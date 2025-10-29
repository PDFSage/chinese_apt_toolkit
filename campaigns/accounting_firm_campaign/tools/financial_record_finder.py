import os
import re

def find_financial_records(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"tax record|audit|financial statement", content, re.IGNORECASE):
                        print(f"Found financial records in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_financial_records(path)

if __name__ == "__main__":
    main()
