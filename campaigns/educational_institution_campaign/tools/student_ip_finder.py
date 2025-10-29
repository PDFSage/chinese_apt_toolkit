import os
import re

def find_student_ip(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"student id|grade|proprietary|confidential", content, re.IGNORECASE):
                        print(f"Found student data or IP in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_student_ip(path)

if __name__ == "__main__":
    main()
