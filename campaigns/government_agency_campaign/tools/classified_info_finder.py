import os
import re

def find_classified_info(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"top secret|secret|classified", content, re.IGNORECASE):
                        print(f"Found classified information in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_classified_info(path)

if __name__ == "__main__":
    main()
