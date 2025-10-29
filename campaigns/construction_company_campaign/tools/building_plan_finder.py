import os
import re

def find_building_plans(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    if re.search(r"building plan|blueprint|project data", content, re.IGNORECASE):
                        print(f"Found building plans or project data in {os.path.join(root, file)}")
            except:
                pass

def main():
    path = input("Enter path to scan: ")
    find_building_plans(path)

if __name__ == "__main__":
    main()
