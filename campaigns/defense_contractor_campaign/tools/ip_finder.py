import os
import re

def find_ip(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"proprietary|confidential|trade secret", content, re.IGNORECASE):
                        print(f"Found intellectual property in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_ip(path)

if __name__ == "__main__":
    main()
