import subprocess
import os

def main():
    # Run the supply chain scanner
    scanner_path = os.path.join(os.path.dirname(__file__), "tools", "supply_chain_scanner.py")
    subprocess.run(["python3", scanner_path])

    # Run the supply chain disruptor
    disruptor_path = os.path.join(os.path.dirname(__file__), "payloads", "supply_chain_disruptor.py")
    subprocess.run(["python3", disruptor_path])

if __name__ == "__main__":
    main()
