import subprocess
import os

def main():
    # Run the nuclear reactor scanner
    nuclear_reactor_scanner_path = os.path.join(os.path.dirname(__file__), "tools", "nuclear_reactor_scanner.py")
    subprocess.run(["python3", nuclear_reactor_scanner_path])

    # Run the meltdown payload
    meltdown_payload_path = os.path.join(os.path.dirname(__file__), "payloads", "meltdown_payload.py")
    subprocess.run(["python3", meltdown_payload_path])

if __name__ == "__main__":
    main()
