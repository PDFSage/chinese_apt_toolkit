import subprocess
import os

def main():
    # Run the power grid scanner
    power_grid_scanner_path = os.path.join(os.path.dirname(__file__), "tools", "power_grid_scanner.py")
    subprocess.run(["python3", power_grid_scanner_path])

    # Run the power grid disruptor
    power_grid_disruptor_path = os.path.join(os.path.dirname(__file__), "payloads", "power_grid_disruptor.py")
    subprocess.run(["python3", power_grid_disruptor_path])

if __name__ == "__main__":
    main()
