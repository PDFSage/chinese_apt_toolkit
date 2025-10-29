import subprocess
import os

def main():
    # Run the VR tech finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "vr_tech_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the VR tech exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "vr_tech_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
