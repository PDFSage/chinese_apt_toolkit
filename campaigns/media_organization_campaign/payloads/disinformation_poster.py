import tweepy
import sys

def post_disinformation(api_key, api_secret, access_token, access_token_secret, message):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)
    print("Posted disinformation")

def main():
    api_key = input("Enter API key: ")
    api_secret = input("Enter API secret: ")
    access_token = input("Enter access token: ")
    access_token_secret = input("Enter access token secret: ")
    message = input("Enter message: ")
    post_disinformation(api_key, api_secret, access_token, access_token_secret, message)

if __name__ == "__main__":
    main()
