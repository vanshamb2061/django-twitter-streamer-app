import tweepy
from tweepy.auth import OAuthHandler
from .models import Tweet
import twitter_credentials


def user_tweets():
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials)
    auth.set_access_token('OAuth Access Token', 'OAuth Access Token Secret')
    api = tweepy.API(auth)
    user_tweets = api.user_timeline(count=50)
    return user_tweets

def save_to_db():
    original_tweets = user_tweets()
    for original_tweet in original_tweets:
        if not original_tweet.retweeted:
            if not Tweet.objects.filter(tweet_id=original_tweet.id):
                new_tweet = Tweet(tweet_id = original_tweet.id, tweet_text = original_tweet.text, published_date = original_tweet.created_at, is_active = True)
                new_tweet.save()