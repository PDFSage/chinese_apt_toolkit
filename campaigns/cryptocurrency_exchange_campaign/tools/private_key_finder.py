import os
import re

def find_private_keys(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"private key|wallet.dat", content, re.IGNORECASE):
                        print(f"Found private key in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_private_keys(path)

if __name__ == "__main__":
    main()
