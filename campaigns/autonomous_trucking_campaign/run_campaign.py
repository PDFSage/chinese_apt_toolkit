import subprocess
import os

def main():
    # Run the autonomous trucking tech finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "autonomous_trucking_tech_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the autonomous truck hijacker
    hijacker_path = os.path.join(os.path.dirname(__file__), "payloads", "autonomous_truck_hijacker.py")
    subprocess.run(["python3", hijacker_path])

if __name__ == "__main__":
    main()
