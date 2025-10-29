import os
import re

def find_genetic_research(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"genetic sequence|crispr|proprietary", content, re.IGNORECASE):
                        print(f"Found genetic research or IP in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_genetic_research(path)

if __name__ == "__main__":
    main()
