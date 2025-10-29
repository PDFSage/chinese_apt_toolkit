/*
APT Network Scanner
Advanced network reconnaissance and scanning tool
For educational and authorized penetration testing only
*/

package main

import (
	"bufio"
	"encoding/json"
	"flag"
	"fmt"
	"net"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"
)

type ScanResult struct {
	IP        string   `json:"ip"`
	Hostname  string   `json:"hostname,omitempty"`
	OpenPorts []int    `json:"open_ports,omitempty"`
	Services  []string `json:"services,omitempty"`
}

type NetworkScanner struct {
	Targets    []string
	Ports      []int
	Threads    int
	Timeout    time.Duration
	OutputFile string
}

func (ns *NetworkScanner) printBanner() {
	banner := `
    ___  _____ _____   _   _      _                      _____                      _             
   / _ \\|  _  |  __ \\ | \\ | |    | |                    /  ___|                    | |            
  / /_\\ \\ | | | |  \\/ |  \\| | ___| |___      _____ _ __\\ \\`--.  ___  __ _ _ __ ___| |_ ___ _ __ 
  |  _  | | | | | __  | . \\` |/ _ \\ __\\ \\ /\\ / / _ \\ '__|\`--. \\/ _ \\/ _\` | '__/ __| __/ _ \\ '__|
  | | | \\ \\_/ / |_\\ \\ | |\\. |  __/ |_ \\ V  V /  __/ |  /\\__/ /  __/ (_| | | | (__| ||  __/ |   
  \\_| |_/\\___/ \\____/ \\_| \\_/\\___|\\__| \\_/\\_/ \\___|_|  \\____/ \\___|\\__,_|_|  \\___|\\__\\___|_|   

                          Advanced Network Scanner
                     For Educational and Authorized Testing Only
`
	fmt.Println(banner)
}

func (ns *NetworkScanner) expandCIDR(cidr string) ([]string, error) {
	ip, ipnet, err := net.ParseCIDR(cidr)
	if err != nil {
		return nil, err
	}

	var ips []string
	for ip := ip.Mask(ipnet.Mask); ipnet.Contains(ip); ns.incrementIP(ip) {
		ips = append(ips, ip.String())
	}

	// Remove network and broadcast addresses
	if len(ips) > 2 {
		ips = ips[1 : len(ips)-1]
	}

	return ips, nil
}

func (ns *NetworkScanner) incrementIP(ip net.IP) {
	for j := len(ip) - 1; j >= 0; j-- {
		ip[j]++
		if ip[j] > 0 {
			break
		}
	}
}

func (ns *NetworkScanner) parseTargets(target string) ([]string, error) {
	var targets []string

	// Check if it's a CIDR notation
	if strings.Contains(target, "/") {
		ips, err := ns.expandCIDR(target)
		if err != nil {
			return nil, err
		}
		targets = append(targets, ips...)
	} else if strings.Contains(target, "-") {
		// IP range (e.g., 192.168.1.1-192.168.1.10)
		parts := strings.Split(target, "-")
		if len(parts) == 2 {
			startIP := net.ParseIP(parts[0])
			endIP := net.ParseIP(parts[1])
			if startIP != nil && endIP != nil {
				for ip := startIP; !ip.Equal(endIP); ns.incrementIP(ip) {
					targets = append(targets, ip.String())
				}
				targets = append(targets, endIP.String())
			}
		}
	} else {
		// Single IP or hostname
		targets = append(targets, target)
	}

	return targets, nil
}

func (ns *NetworkScanner) parsePorts(portSpec string) ([]int, error) {
	var ports []int

	if portSpec == "" {
		// Default common ports
		return []int{21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080}, nil
	}

	if strings.Contains(portSpec, "-") {
		// Port range
		parts := strings.Split(portSpec, "-")
		if len(parts) == 2 {
			start, err1 := strconv.Atoi(parts[0])
			end, err2 := strconv.Atoi(parts[1])
			if err1 == nil && err2 == nil && start <= end {
				for port := start; port <= end; port++ {
					ports = append(ports, port)
				}
			}
		}
	} else if strings.Contains(portSpec, ",") {
		// Comma-separated ports
		parts := strings.Split(portSpec, ",")
		for _, part := range parts {
			port, err := strconv.Atoi(strings.TrimSpace(part))
			if err == nil && port >= 1 && port <= 65535 {
				ports = append(ports, port)
			}
		}
	} else {
		// Single port
		port, err := strconv.Atoi(portSpec)
		if err == nil && port >= 1 && port <= 65535 {
			ports = append(ports, port)
		}
	}

	return ports, nil
}

func (ns *NetworkScanner) scanPort(ip string, port int, results chan<- ScanResult) {
	address := fmt.Sprintf("%s:%d", ip, port)
	
	conn, err := net.DialTimeout("tcp", address, ns.Timeout)
	if err != nil {
		return
	}
	conn.Close()

	// Get hostname if possible
	hostnames, _ := net.LookupAddr(ip)
	hostname := ""
	if len(hostnames) > 0 {
		hostname = strings.TrimSuffix(hostnames[0], ".")
	}

	// Determine service based on port
	service := ns.getServiceName(port)

	results <- ScanResult{
		IP:        ip,
		Hostname:  hostname,
		OpenPorts: []int{port},
		Services:  []string{service},
	}
}

func (ns *NetworkScanner) getServiceName(port int) string {
	serviceMap := map[int]string{
		21:   "FTP",
		22:   "SSH",
		23:   "Telnet",
		25:   "SMTP",
		53:   "DNS",
		80:   "HTTP",
		110:  "POP3",
		135:  "RPC",
		139:  "NetBIOS",
		143:  "IMAP",
		443:  "HTTPS",
		445:  "SMB",
		993:  "IMAPS",
		995:  "POP3S",
		1723: "PPTP",
		3306: "MySQL",
		3389: "RDP",
		5900: "VNC",
		8080: "HTTP-Alt",
	}

	if service, exists := serviceMap[port]; exists {
		return service
	}
	return "Unknown"
}

func (ns *NetworkScanner) scanHost(ip string, results chan<- ScanResult) {
	var wg sync.WaitGroup
	portResults := make(chan int, len(ns.Ports))

	// Scan all ports for this host
	for _, port := range ns.Ports {
		wg.Add(1)
		go func(p int) {
			defer wg.Done()
			ns.scanPort(ip, p, results)
		}(port)
	}

	wg.Wait()
	close(portResults)
}

func (ns *NetworkScanner) Run() []ScanResult {
	var results []ScanResult
	resultChan := make(chan ScanResult, len(ns.Targets)*len(ns.Ports))
	var wg sync.WaitGroup

	// Process targets
	for _, target := range ns.Targets {
		parsedTargets, err := ns.parseTargets(target)
		if err != nil {
			fmt.Printf("[-] Error parsing target %s: %v\n", target, err)
			continue
		}

		for _, ip := range parsedTargets {
			wg.Add(1)
			go func(host string) {
				defer wg.Done()
				ns.scanHost(host, resultChan)
			}(ip)
		}
	}

	// Wait for all scans to complete
	go func() {
		wg.Wait()
		close(resultChan)
	}()

	// Collect results
	for result := range resultChan {
		results = append(results, result)
	}

	return results
}

func (ns *NetworkScanner) saveResults(results []ScanResult) error {
	if ns.OutputFile == "" {
		return nil
	}

	file, err := os.Create(ns.OutputFile)
	if err != nil {
		return err
	}
	defer file.Close()

	encoder := json.NewEncoder(file)
	encoder.SetIndent("", "  ")
	
	return encoder.Encode(results)
}

func (ns *NetworkScanner) printResults(results []ScanResult) {
	fmt.Printf("\n[*] Scan Results:\n")
	fmt.Printf("%-15s %-30s %-20s %s\n", "IP", "Hostname", "Open Ports", "Services")
	fmt.Printf("%-15s %-30s %-20s %s\n", strings.Repeat("-", 15), strings.Repeat("-", 30), strings.Repeat("-", 20), strings.Repeat("-", 20))

	// Group results by IP
	resultsByIP := make(map[string]*ScanResult)
	for _, result := range results {
		if existing, exists := resultsByIP[result.IP]; exists {
			existing.OpenPorts = append(existing.OpenPorts, result.OpenPorts...)
			existing.Services = append(existing.Services, result.Services...)
		} else {
			resultsByIP[result.IP] = &result
		}
	}

	for _, result := range resultsByIP {
		portsStr := ""
		for i, port := range result.OpenPorts {
			if i > 0 {
				portsStr += ","
			}
			portsStr += strconv.Itoa(port)
		}

		servicesStr := ""
		for i, service := range result.Services {
			if i > 0 {
				servicesStr += ","
			}
			servicesStr += service
		}

		fmt.Printf("%-15s %-30s %-20s %s\n", result.IP, result.Hostname, portsStr, servicesStr)
	}
}

func main() {
	var (
		target   = flag.String("t", "", "Target IP, range, or CIDR (e.g., 192.168.1.1, 192.168.1.1-100, 192.168.1.0/24)")
		ports    = flag.String("p", "", "Ports to scan (e.g., 80,443, 1-1000, or common for common ports)")
		threads  = flag.Int("threads", 100, "Number of concurrent threads")
		timeout  = flag.Int("timeout", 2, "Connection timeout in seconds")
		output   = flag.String("o", "", "Output file for JSON results")
		file     = flag.String("f", "", "File containing list of targets")
	)

	flag.Parse()

	scanner := &NetworkScanner{
		Threads: *threads,
		Timeout: time.Duration(*timeout) * time.Second,
		OutputFile: *output,
	}

	scanner.printBanner()

	// Parse targets
	if *target != "" {
		scanner.Targets = append(scanner.Targets, *target)
	}

	if *file != "" {
		file, err := os.Open(*file)
		if err != nil {
			fmt.Printf("[-] Error opening file: %v\n", err)
			os.Exit(1)
		}
		defer file.Close()

		scannerFile := bufio.NewScanner(file)
		for scannerFile.Scan() {
			target := strings.TrimSpace(scannerFile.Text())
			if target != "" {
				scanner.Targets = append(scanner.Targets, target)
			}
		}
	}

	if len(scanner.Targets) == 0 {
		fmt.Println("[-] No targets specified. Use -t or -f to specify targets.")
		flag.Usage()
		os.Exit(1)
	}

	// Parse ports
	var err error
	scanner.Ports, err = scanner.parsePorts(*ports)
	if err != nil {
		fmt.Printf("[-] Error parsing ports: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("[*] Starting scan with %d threads\n", scanner.Threads)
	fmt.Printf("[*] Scanning %d target(s) and %d port(s)\n", len(scanner.Targets), len(scanner.Ports))
	fmt.Printf("[*] Timeout: %v\n", scanner.Timeout)
	fmt.Println()

	results := scanner.Run()

	// Print results
	scanner.printResults(results)

	// Save results if output file specified
	if *output != "" {
		err := scanner.saveResults(results)
		if err != nil {
			fmt.Printf("[-] Error saving results: %v\n", err)
		} else {
			fmt.Printf("\n[+] Results saved to: %s\n", *output)
		}
	}

	fmt.Printf("\n[+] Scan completed. Found %d open ports.\n", len(results))
}