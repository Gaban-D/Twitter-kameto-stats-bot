from dotenv import load_dotenv
from pprint import pprint
import tweepy
import os

load_dotenv()

auth = tweepy.OAuthHandler(os.environ.get("twitter_consumer_public"), os.environ.get("twitter_consumer_secret"))

try:
	redirect_url = auth.get_authorization_url()
	print(redirect_url)
except tweepy.TweepError:
	print('Error! Failed to get request token. Please verify your twitter consumer public and secret keys')
	quit()

verifier = input("Enter the code given by twitter website: ")

try:
	tokens = auth.get_access_token(verifier)
	pprint(tokens)
except tweepy.TweepError:
	print('Error! Failed to get access token. Please verify the code you entered')
	exit()
