import subprocess
import os

def main():
    # Run the autonomous shipping tech finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "autonomous_shipping_tech_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the autonomous ship hijacker
    hijacker_path = os.path.join(os.path.dirname(__file__), "payloads", "autonomous_ship_hijacker.py")
    subprocess.run(["python3", hijacker_path])

if __name__ == "__main__":
    main()
