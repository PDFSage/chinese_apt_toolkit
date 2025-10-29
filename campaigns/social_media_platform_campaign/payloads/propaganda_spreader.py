import instaloader
import sys

def spread_propaganda(username, password, target_username, message):
    L = instaloader.Instaloader()
    L.login(username, password)
    profile = instaloader.Profile.from_username(L.context, target_username)
    for post in profile.get_posts():
        post.add_comment(message)
        break

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    target_username = input("Enter target username: ")
    message = input("Enter message: ")
    spread_propaganda(username, password, target_username, message)

if __name__ == "__main__":
    main()
