import os
import re

def find_financial_data(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"account number|credit card|social security number", content, re.IGNORECASE):
                        print(f"Found sensitive data in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_financial_data(path)

if __name__ == "__main__":
    main()
