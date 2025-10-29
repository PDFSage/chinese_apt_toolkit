import os
import re

def find_3d_models(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith((".stl", ".obj", ".fbx", ".3ds")):
                print(f"Found 3D model in {os.path.join(root, file)}")

def main():
    path = input("Enter path to scan: ")
    find_3d_models(path)

if __name__ == "__main__":
    main()
