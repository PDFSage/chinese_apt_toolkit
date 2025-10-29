import subprocess
import os

def main():
    # Run the satellite scanner
    satellite_scanner_path = os.path.join(os.path.dirname(__file__), "tools", "satellite_scanner.py")
    subprocess.run(["python3", satellite_scanner_path])

    # Run the satellite disruptor
    satellite_disruptor_path = os.path.join(os.path.dirname(__file__), "payloads", "satellite_disruptor.py")
    subprocess.run(["python3", satellite_disruptor_path])

if __name__ == "__main__":
    main()
