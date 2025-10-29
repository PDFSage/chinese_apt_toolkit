import instaloader
import sys

def harvest_user_data(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    for post in profile.get_posts():
        L.download_post(post, target=profile.username)

def main():
    username = input("Enter username to harvest: ")
    harvest_user_data(username)

if __name__ == "__main__":
    main()
