import tweepy
from sys import exit
from datetime import datetime as dt
from time import sleep
import requests
from credentials import *

# Authenticate to Twitter
try:
    auth = tweepy.OAuthHandler(API_key, API_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.verify_credentials()
except:
    exit("Twitter Verification Failure")

# Make tweet
def make_tweet():
    try:
        api.update_status_with_media(status="Test", filename="current_photo.jpg")
        return 1
    except:
        return 0

# Main code to run
def main():
    if not make_tweet():
        exit("Tweet Creation Failure")

if __name__ == "__main__":
    main()
