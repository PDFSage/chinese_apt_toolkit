import subprocess
import os

def main():
    # Run the 911 scanner
    scanner_path = os.path.join(os.path.dirname(__file__), "tools", "911_scanner.py")
    subprocess.run(["python3", scanner_path])

    # Run the 911 disruptor
    disruptor_path = os.path.join(os.path.dirname(__file__), "payloads", "911_disruptor.py")
    subprocess.run(["python3", disruptor_path])

if __name__ == "__main__":
    main()
