import subprocess
import os

def main():
    # Run the transportation scanner
    transportation_scanner_path = os.path.join(os.path.dirname(__file__), "tools", "transportation_scanner.py")
    subprocess.run(["python3", transportation_scanner_path])

    # Run the transportation disruptor
    transportation_disruptor_path = os.path.join(os.path.dirname(__file__), "payloads", "transportation_disruptor.py")
    subprocess.run(["python3", transportation_disruptor_path])

if __name__ == "__main__":
    main()
