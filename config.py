import tweepy
import os
from dotenv import load_dotenv
from twitchAPI.twitch import Twitch

load_dotenv()


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
