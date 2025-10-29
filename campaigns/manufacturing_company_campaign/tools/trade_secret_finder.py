import os
import re

def find_trade_secrets(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"trade secret|proprietary|formula", content, re.IGNORECASE):
                        print(f"Found trade secret in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_trade_secrets(path)

if __name__ == "__main__":
    main()
