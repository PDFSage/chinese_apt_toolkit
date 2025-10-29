import subprocess
import os

def main():
    # Run the autonomous drone tech finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "autonomous_drone_tech_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the autonomous drone hijacker
    hijacker_path = os.path.join(os.path.dirname(__file__), "payloads", "autonomous_drone_hijacker.py")
    subprocess.run(["python3", hijacker_path])

if __name__ == "__main__":
    main()
