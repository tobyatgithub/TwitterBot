import tweepy
import tkinter
from credentials import credentials
print("hello stranger")

consumer_key = credentials.get("API_key")
consumer_secret = credentials.get("secret_key")
access_token = credentials.get("Access_token")
access_token_secret = credentials.get("Access_token_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)

public_tweets = api.home_timeline()
# import pdb; pdb.set_trace()
for tweet in public_tweets:
    print(tweet.text)