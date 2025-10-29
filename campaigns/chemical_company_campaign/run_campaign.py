import subprocess
import os

def main():
    # Run the chemical formula finder
    finder_path = os.path.join(os.path.dirname(__file__), "tools", "chemical_formula_finder.py")
    subprocess.run(["python3", finder_path])

    # Run the chemical production disruptor
    disruptor_path = os.path.join(os.path.dirname(__file__), "payloads", "chemical_production_disruptor.py")
    subprocess.run(["python3", disruptor_path])

if __name__ == "__main__":
    main()
