import os
import re

def find_drone_tech(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"drone|unmanned aerial vehicle|proprietary", content, re.IGNORECASE):
                        print(f"Found drone tech in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_drone_tech(path)

if __name__ == "__main__":
    main()
