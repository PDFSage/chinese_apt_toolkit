import subprocess
import os

def main():
    # Run the ICS scanner
    ics_scanner_path = os.path.join(os.path.dirname(__file__), "tools", "ics_scanner.py")
    subprocess.run(["python3", ics_scanner_path])

    # Run the ICS disruptor
    ics_disruptor_path = os.path.join(os.path.dirname(__file__), "payloads", "ics_disruptor.py")
    subprocess.run(["python3", ics_disruptor_path])

if __name__ == "__main__":
    main()
