import subprocess
import os

def main():
    # Run the AIS scanner
    ais_scanner_path = os.path.join(os.path.dirname(__file__), "tools", "ais_scanner.py")
    subprocess.run(["python3", ais_scanner_path])

    # Run the shipping disruptor
    shipping_disruptor_path = os.path.join(os.path.dirname(__file__), "payloads", "shipping_disruptor.py")
    subprocess.run(["python3", shipping_disruptor_path])

if __name__ == "__main__":
    main()
