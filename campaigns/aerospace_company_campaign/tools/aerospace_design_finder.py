import os
import re

def find_aerospace_designs(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"aerospace design|blueprint|proprietary", content, re.IGNORECASE):
                        print(f"Found aerospace design or IP in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_aerospace_designs(path)

if __name__ == "__main__":
    main()
