import tweepy
from sys import exit
from time import sleep
from credentials import *

# Authenticate to Twitter
try:
    auth = tweepy.OAuthHandler(API_key, API_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.verify_credentials()
except:
    exit("Twitter Verification Failure")

# Get the next frame filename
def next_frame(frame_number: int) -> str:
    return "frame" + str(frame_number + 1) + ".jpg"


# Make tweet
def make_tweet(text: str, frame: str):
    try:
        api.update_status_with_media(status=text, filename=frame)
        return 1
    except:
        return 0

# Main code to run
def main():
    if not make_tweet():
        exit("Tweet Creation Failure")

if __name__ == "__main__":
    main()
