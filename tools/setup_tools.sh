#!/bin/bash

# APT Tools Setup Script
# Automated setup for all APT toolkit tools
# For educational and authorized penetration testing only

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Banner
echo -e "${BLUE}"
echo "  ___  _____ _____   _____           _           _                 _       "
echo " / _ \\|  _  |  __ \\ /  ___|         | |         | |               | |      "
echo "/ /_\\ \\ | | | |  \\/ \\ \\`--.  ___  | | ___  ___| |_ ___  ___  ___| | ___  "
echo "|  _  | | | | | __   \\ \\`--. \\/ _ \\ | |/ _ \\/ __| __/ _ \\/ __|/ _ \\ |"
echo "| | | \\ \\_/ / |_\\ \\/\\__/ /  __/ | |  __/ (__| || (_) \\__ \\  __/ |"
echo "\\_| |_/\\___/ \\____/ \\____/ \\___| |_|\\___|\\___|\\__\\___/|___/\\___|_|"
echo ""
echo "                    APT Tools Setup Script"
echo "           For Educational and Authorized Testing Only"
echo -e "${NC}"

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install package (Debian/Ubuntu)
install_package() {
    local package=$1
    echo -e "${YELLOW}[*] Installing $package...${NC}"
    if command_exists apt-get; then
        sudo apt-get update && sudo apt-get install -y "$package"
    elif command_exists yum; then
        sudo yum install -y "$package"
    elif command_exists brew; then
        brew install "$package"
    else
        echo -e "${RED}[-] Package manager not found. Please install $package manually.${NC}"
        return 1
    fi
}

# Function to check and install dependencies
check_dependencies() {
    echo -e "${BLUE}[*] Checking dependencies...${NC}"
    
    local missing_deps=()
    
    # Required tools
    local required_tools=("python3" "node" "ruby" "gcc" "go" "powershell")
    
    for tool in "${required_tools[@]}"; do
        if ! command_exists "$tool"; then
            missing_deps+=("$tool")
        fi
    done
    
    # Optional but recommended tools
    local recommended_tools=("nmap" "whois" "dig" "curl" "git")
    
    for tool in "${recommended_tools[@]}"; do
        if ! command_exists "$tool"; then
            echo -e "${YELLOW}[!] Recommended tool not found: $tool${NC}"
        fi
    done
    
    if [ ${#missing_deps[@]} -ne 0 ]; then
        echo -e "${RED}[-] Missing required dependencies: ${missing_deps[*]}${NC}"
        echo -e "${YELLOW}[*] Attempting to install missing dependencies...${NC}"
        
        for dep in "${missing_deps[@]}"; do
            case $dep in
                "python3")
                    install_package "python3 python3-pip"
                    ;;
                "node")
                    install_package "nodejs npm"
                    ;;
                "ruby")
                    install_package "ruby"
                    ;;
                "gcc")
                    install_package "gcc"
                    ;;
                "go")
                    install_package "golang"
                    ;;
                "powershell")
                    if command_exists apt-get; then
                        # Install PowerShell on Debian/Ubuntu
                        wget -q https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb
                        sudo dpkg -i packages-microsoft-prod.deb
                        sudo apt-get update
                        sudo apt-get install -y powershell
                        rm packages-microsoft-prod.deb
                    else
                        echo -e "${RED}[-] Please install PowerShell manually for your distribution${NC}"
                    fi
                    ;;
            esac
        done
    else
        echo -e "${GREEN}[+] All required dependencies are installed${NC}"
    fi
}

# Function to compile C tools
compile_c_tools() {
    echo -e "${BLUE}[*] Compiling C tools...${NC}"
    
    if command_exists gcc; then
        if [ -f "apt_memory_injector.c" ]; then
            echo -e "${YELLOW}[*] Compiling apt_memory_injector...${NC}"
            gcc -o apt_memory_injector apt_memory_injector.c -lpsapi
            if [ $? -eq 0 ]; then
                echo -e "${GREEN}[+] apt_memory_injector compiled successfully${NC}"
            else
                echo -e "${RED}[-] Failed to compile apt_memory_injector${NC}"
            fi
        else
            echo -e "${RED}[-] apt_memory_injector.c not found${NC}"
        fi
    else
        echo -e "${RED}[-] GCC not available, skipping C compilation${NC}"
    fi
}

# Function to compile Go tools
compile_go_tools() {
    echo -e "${BLUE}[*] Compiling Go tools...${NC}"
    
    if command_exists go; then
        if [ -f "apt_network_scanner.go" ]; then
            echo -e "${YELLOW}[*] Compiling apt_network_scanner...${NC}"
            go build apt_network_scanner.go
            if [ $? -eq 0 ]; then
                echo -e "${GREEN}[+] apt_network_scanner compiled successfully${NC}"
            else
                echo -e "${RED}[-] Failed to compile apt_network_scanner${NC}"
            fi
        else
            echo -e "${RED}[-] apt_network_scanner.go not found${NC}"
        fi
    else
        echo -e "${RED}[-] Go compiler not available, skipping Go compilation${NC}"
    fi
}

# Function to set executable permissions
set_permissions() {
    echo -e "${BLUE}[*] Setting executable permissions...${NC}"
    
    # Shell scripts
    chmod +x *.sh 2>/dev/null || true
    
    # Python scripts
    chmod +x *.py 2>/dev/null || true
    
    # Ruby scripts
    chmod +x *.rb 2>/dev/null || true
    
    # JavaScript files (make them executable if needed)
    for js_file in *.js; do
        if [ -f "$js_file" ]; then
            echo "#!/usr/bin/env node" | cat - "$js_file" > temp && mv temp "$js_file"
            chmod +x "$js_file"
        fi
    done
    
    echo -e "${GREEN}[+] Permissions set successfully${NC}"
}

# Function to install Python dependencies
install_python_deps() {
    echo -e "${BLUE}[*] Checking Python dependencies...${NC}"
    
    if command_exists python3; then
        # Check if pip is available
        if python3 -m pip --version >/dev/null 2>&1; then
            echo -e "${GREEN}[+] Python pip is available${NC}"
        else
            echo -e "${YELLOW}[!] Installing pip for Python3...${NC}"
            if command_exists apt-get; then
                sudo apt-get install -y python3-pip
            fi
        fi
    fi
}

# Function to install Node.js dependencies
install_node_deps() {
    echo -e "${BLUE}[*] Checking Node.js dependencies...${NC}"
    
    if command_exists npm; then
        echo -e "${GREEN}[+] npm is available${NC}"
        # No external dependencies needed for our Node.js tool
    fi
}

# Function to verify tool functionality
verify_tools() {
    echo -e "${BLUE}[*] Verifying tool functionality...${NC}"
    
    local tools_verified=0
    local total_tools=0
    
    # Check each tool
    for tool in apt_recon.sh APT-PowerShell-Toolkit.ps1 apt_persistence.py apt_web_recon.js apt_social_engineering.rb; do
        if [ -f "$tool" ]; then
            total_tools=$((total_tools + 1))
            if [ -x "$tool" ]; then
                echo -e "${GREEN}[+] $tool is ready${NC}"
                tools_verified=$((tools_verified + 1))
            else
                echo -e "${YELLOW}[!] $tool is not executable${NC}"
            fi
        fi
    done
    
    # Check compiled tools
    for tool in apt_memory_injector apt_network_scanner; do
        if [ -f "$tool" ]; then
            total_tools=$((total_tools + 1))
            if [ -x "$tool" ]; then
                echo -e "${GREEN}[+] $tool is ready${NC}"
                tools_verified=$((tools_verified + 1))
            else
                echo -e "${YELLOW}[!] $tool is not executable${NC}"
            fi
        fi
    done
    
    echo -e "${GREEN}[+] $tools_verified out of $total_tools tools are ready${NC}"
}

# Function to display usage information
show_usage() {
    echo -e "${BLUE}Usage: $0 [OPTIONS]${NC}"
    echo ""
    echo "OPTIONS:"
    echo "  --help              Show this help message"
    echo "  --deps-only         Only install dependencies"
    echo "  --compile-only      Only compile tools"
    echo "  --verify-only       Only verify existing tools"
    echo ""
    echo "EXAMPLES:"
    echo "  $0                    # Full setup"
    echo "  $0 --deps-only        # Install dependencies only"
    echo "  $0 --compile-only     # Compile tools only"
    echo ""
}

# Main execution
main() {
    local deps_only=false
    local compile_only=false
    local verify_only=false
    
    # Parse command line arguments
    for arg in "$@"; do
        case $arg in
            --help)
                show_usage
                exit 0
                ;;
            --deps-only)
                deps_only=true
                ;;
            --compile-only)
                compile_only=true
                ;;
            --verify-only)
                verify_only=true
                ;;
        esac
    done
    
    if [ "$verify_only" = true ]; then
        verify_tools
        exit 0
    fi
    
    if [ "$deps_only" = true ]; then
        check_dependencies
        install_python_deps
        install_node_deps
        exit 0
    fi
    
    if [ "$compile_only" = true ]; then
        compile_c_tools
        compile_go_tools
        exit 0
    fi
    
    # Full setup
    echo -e "${GREEN}[+] Starting full APT tools setup${NC}"
    
    check_dependencies
    install_python_deps
    install_node_deps
    compile_c_tools
    compile_go_tools
    set_permissions
    verify_tools
    
    echo -e "${GREEN}[+] APT tools setup completed successfully!${NC}"
    echo ""
    echo -e "${BLUE}Next steps:${NC}"
    echo "  1. Review the tools/README.md for usage instructions"
    echo "  2. Ensure you have proper authorization for testing"
    echo "  3. Test tools in an isolated environment first"
    echo "  4. Follow ethical guidelines and legal requirements"
    echo ""
}

# Check if script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi