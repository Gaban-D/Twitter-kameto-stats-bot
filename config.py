import tweepy
import sys
import os
import locale
from dotenv import load_dotenv
from pathlib import Path
from twitchAPI.twitch import Twitch

load_dotenv()
locale.setlocale(locale.LC_ALL, 'French')
save_path = Path(sys.argv[0]).parent / Path('saved_variables')

twitch_channel = 'THE_TWITCH_CHANNEL_YOU_WANT_TO_TRACK'

def get_twitter_api():
    api_consumer_key = os.environ.get("twitter_consumer_public")
    api_consumer_secret = os.environ.get("twitter_consumer_secret")
    api_access_token = os.environ.get("twitter_access_public")
    api_access_secret = os.environ.get("twitter_access_private")

    auth = tweepy.OAuthHandler(api_consumer_key, api_consumer_secret)
    auth.set_access_token(api_access_token, api_access_secret)

    return tweepy.API(auth)


def get_twitch_api():
    public_token = os.environ.get("twitch_public_token")
    private_token = os.environ.get("twitch_private_token")
    return Twitch(public_token, private_token)
