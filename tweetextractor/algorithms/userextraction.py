import tweepy
from tweepy import OAuthHandler, Stream, API, Cursor
from ..models import Tweet, TwitterAccounts
import twitter_credentials
from tweepy.streaming import StreamListener
import re
import preprocessor as p
from .tweetextraction import TwitterClient

def add_account(name):
    twitter_client = TwitterClient()
    api = twitter_client.get_twitter_client_api()
    screen_name = name
    author = api.get_user(screen_name)
    account = TwitterAccounts(twitter_user_id=author.id, twitter_name=author.name, twitter_screen_name=author.screen_name, twitter_location=author.location)
    account.save()



