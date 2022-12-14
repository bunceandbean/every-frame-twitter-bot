import tweepy
from sys import exit
from time import sleep
import requests
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
    return f"frame{frame_number}.jpg"

# Make tweet
def make_tweet(text: str, frame: str) -> int:
    try:
        api.update_status_with_media(status=text, filename=frame)
        return 1
    except:
        return 0

# Main code to run
def main():

    # Read from frame file and start from next frame in case of crash
    frame_file = open(f"{FILEPATH}last_frame.txt", 'r+')
    starting_frame = int(frame_file.readline().rstrip()) + 1
    frame_file.close()

    # For loop being used to iterate through frame numbers - faster than file i/o
    for i in range(starting_frame, FRAME_AMOUNT):
        text = f"{VIDEO_TITLE} - Frame {i+1}/{FRAME_AMOUNT}"
        if not make_tweet(text, f"{FILEPATH}frames/{next_frame(i)}"):
            exit("Tweet Creation Failure")
        frame_file = open(f"{FILEPATH}last_frame.txt", 'r+')
        frame_file.truncate(0)
        frame_file.write(f"{i}")
        frame_file.close()
        sleep(POST_FREQUENCY_IN_SECONDS)

    print("Process Completed")

if __name__ == "__main__":
    main()
    sleep(600)
