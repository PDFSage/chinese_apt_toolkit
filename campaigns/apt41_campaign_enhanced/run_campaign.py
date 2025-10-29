import subprocess
import os

def main():
    # Run the vulnerability scanner
    vulnerability_scanner_path = os.path.join(os.path.dirname(__file__), "tools", "vulnerability_scanner.py")
    subprocess.run(["python3", vulnerability_scanner_path])

    # Run the exploit
    exploit_path = os.path.join(os.path.dirname(__file__), "payloads", "exploit.py")
    subprocess.run(["python3", exploit_path])

if __name__ == "__main__":
    main()
