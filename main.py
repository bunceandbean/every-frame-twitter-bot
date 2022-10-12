import tweepy
from sys import exit
from time import sleep
from user_values.credentials import *
from user_values.constants import *

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
def make_tweet(text: str, frame: str) -> int:
    try:
        api.update_status_with_media(status=text, filename=frame)
        return 1
    except:
        return 0

# Main code to run
def main():
    for i in range(FRAME_AMOUNT):
        text = VIDEO_TITLE + " - Frame " + str(i+1) + "/" + str(FRAME_AMOUNT)
        if not make_tweet(text, "frames/frame" + str(i) + ".jpg"):
            exit("Tweet Creation Failure")
        sleep(POST_FREQUENCY_IN_SECONDS)

if __name__ == "__main__":
    main()
