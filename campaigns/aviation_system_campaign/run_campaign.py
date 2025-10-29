import subprocess
import os

def main():
    # Run the ADS-B scanner
    adsb_scanner_path = os.path.join(os.path.dirname(__file__), "tools", "adsb_scanner.py")
    subprocess.run(["python3", adsb_scanner_path])

    # Run the ATC disruptor
    atc_disruptor_path = os.path.join(os.path.dirname(__file__), "payloads", "atc_disruptor.py")
    subprocess.run(["python3", atc_disruptor_path])

if __name__ == "__main__":
    main()
