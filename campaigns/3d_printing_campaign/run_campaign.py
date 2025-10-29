import subprocess
import os

def main():
    # Run the 3D model finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "3d_model_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the 3D model exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "3d_model_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
