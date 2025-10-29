import os
import re

def find_customer_data(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"customer name|billing address|credit card", content, re.IGNORECASE):
                        print(f"Found customer data in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_customer_data(path)

if __name__ == "__main__":
    main()
