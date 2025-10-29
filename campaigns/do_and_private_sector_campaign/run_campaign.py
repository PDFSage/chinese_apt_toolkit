import subprocess
import os

def main():
    # Start the C2 server in the background
    c2_server_path = os.path.join(os.path.dirname(__file__), "tools", "c2_server.py")
    subprocess.Popen(["python3", c2_server_path])

    # Run the spear phishing generator
    spear_phishing_generator_path = os.path.join(os.path.dirname(__file__), "tools", "spear_phishing_generator.py")
    payload_path = os.path.join(os.path.dirname(__file__), "payloads", "payload")
    subprocess.run(["python3", spear_phishing_generator_path, payload_path])

if __name__ == "__main__":
    main()
