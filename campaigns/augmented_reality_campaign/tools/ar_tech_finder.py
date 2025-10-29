import os
import re

def find_ar_tech(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"augmented reality|computer vision|user data", content, re.IGNORECASE):
                        print(f"Found AR tech or user data in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_ar_tech(path)

if __name__ == "__main__":
    main()
