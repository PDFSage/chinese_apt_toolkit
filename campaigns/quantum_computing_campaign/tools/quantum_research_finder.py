import os
import re

def find_quantum_research(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"quantum computing|qubit|proprietary", content, re.IGNORECASE):
                        print(f"Found quantum computing research in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_quantum_research(path)

if __name__ == "__main__":
    main()
