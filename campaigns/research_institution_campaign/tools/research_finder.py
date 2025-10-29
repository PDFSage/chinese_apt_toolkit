import os
import re

def find_research(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"research|study|clinical trial", content, re.IGNORECASE):
                        print(f"Found scientific research in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_research(path)

if __name__ == "__main__":
    main()
