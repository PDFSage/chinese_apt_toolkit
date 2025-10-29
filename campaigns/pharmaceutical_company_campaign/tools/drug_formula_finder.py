import os
import re

def find_drug_formulas(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"drug formula|clinical trial|research data", content, re.IGNORECASE):
                        print(f"Found drug formula or research data in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_drug_formulas(path)

if __name__ == "__main__":
    main()
