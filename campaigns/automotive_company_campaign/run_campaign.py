import subprocess
import os

def main():
    # Run the AV tech finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "av_tech_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the AV tech exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "av_tech_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
