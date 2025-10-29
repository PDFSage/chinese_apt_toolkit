import os
import re

def find_source_user_data(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"source code|password|username", content, re.IGNORECASE):
                        print(f"Found source code or user data in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_source_user_data(path)

if __name__ == "__main__":
    main()
