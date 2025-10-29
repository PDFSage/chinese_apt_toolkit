import subprocess
import os

def main():
    # Run the social media finder
    social_media_finder_path = os.path.join(os.path.dirname(__file__), "tools", "social_media_finder.py")
    subprocess.run(["python3", social_media_finder_path])

    # Run the disinformation poster
    disinformation_poster_path = os.path.join(os.path.dirname(__file__), "payloads", "disinformation_poster.py")
    subprocess.run(["python3", disinformation_poster_path])

if __name__ == "__main__":
    main()
