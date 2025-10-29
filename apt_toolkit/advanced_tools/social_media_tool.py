import tweepy

def post_tweet(api_key, api_secret, access_token, access_token_secret, message):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)
    print("Tweeted successfully")

def main():
    api_key = input("Enter API key: ")
    api_secret = input("Enter API secret: ")
    access_token = input("Enter access token: ")
    access_token_secret = input("Enter access token secret: ")
    message = input("Enter message: ")
    post_tweet(api_key, api_secret, access_token, access_token_secret, message)

if __name__ == "__main__":
    main()
