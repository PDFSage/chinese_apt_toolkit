import os
import re

def find_patient_data(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"patient name|date of birth|medical record number", content, re.IGNORECASE):
                        print(f"Found patient data in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_patient_data(path)

if __name__ == "__main__":
    main()
