import subprocess
import os

def main():
    # Run the drone tech finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "drone_tech_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the drone hijacker
    hijacker_path = os.path.join(os.path.dirname(__file__), "payloads", "drone_hijacker.py")
    subprocess.run(["python3", hijacker_path])

if __name__ == "__main__":
    main()
