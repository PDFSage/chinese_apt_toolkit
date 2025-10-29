import subprocess
import os

def main():
    # Run the agricultural scanner
    agricultural_scanner_path = os.path.join(os.path.dirname(__file__), "tools", "agricultural_scanner.py")
    subprocess.run(["python3", agricultural_scanner_path])

    # Run the food supply disruptor
    food_supply_disruptor_path = os.path.join(os.path.dirname(__file__), "payloads", "food_supply_disruptor.py")
    subprocess.run(["python3", food_supply_disruptor_path])

if __name__ == "__main__":
    main()
