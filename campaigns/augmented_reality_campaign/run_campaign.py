import subprocess
import os

def main():
    # Run the AR tech finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "ar_tech_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the AR tech exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "ar_tech_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
