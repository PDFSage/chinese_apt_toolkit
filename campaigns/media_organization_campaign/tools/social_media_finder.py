from googlesearch import search
import sys

def find_social_media(target):
    for url in search(f"{target} social media", stop=10):
        print(url)

def main():
    target = input("Enter target name: ")
    find_social_media(target)

if __name__ == "__main__":
    main()
