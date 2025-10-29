import os
import re

def find_chemical_formulas(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"chemical formula|proprietary|compound", content, re.IGNORECASE):
                        print(f"Found chemical formula in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_chemical_formulas(path)

if __name__ == "__main__":
    main()
