import subprocess
import os

def main():
    # Run the cloud scanner
    scanner_path = os.path.join(os.path.dirname(__file__), "tools", "cloud_scanner.py")
    subprocess.run(["python3", scanner_path])

    # Run the cloud disruptor
    disruptor_path = os.path.join(os.path.dirname(__file__), "payloads", "cloud_disruptor.py")
    subprocess.run(["python3", disruptor_path])

if __name__ == "__main__":
    main()
