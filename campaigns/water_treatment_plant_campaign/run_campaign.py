import subprocess
import os

def main():
    # Run the water treatment scanner
    water_treatment_scanner_path = os.path.join(os.path.dirname(__file__), "tools", "water_treatment_scanner.py")
    subprocess.run(["python3", water_treatment_scanner_path])

    # Run the poison water supply payload
    poison_water_supply_payload_path = os.path.join(os.path.dirname(__file__), "payloads", "poison_water_supply_payload.py")
    subprocess.run(["python3", poison_water_supply_payload_path])

if __name__ == "__main__":
    main()
