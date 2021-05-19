import tweepy
from tweepy import OAuthHandler, Stream, API, Cursor
from .models import Tweet
import twitter_credentials
from tweepy.streaming import StreamListener
import re

# Twitter Client
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user
    
    def clean_tweet(self,tweet):
        #removing special characters, links from tweet i.e. cleaning
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_twitter_client_api(self):
        return self.twitter_client    
    
    def get_user_timeline_tweets(self,num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline,id=self.twitter_user).items(num_tweets):
            cleaned_tweet=self.clean_tweet(tweet)
            tweets.append(cleaned_tweet)
        return tweets

    def get_friend_list(self,num_friends):
        friend_list=[]
        for friend in Cursor(self.twitter_client.friends,id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list
    
    def get_home_timeline(self,num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline,id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets





#Twitter Authenticator
class TwitterAuthenticator():
    
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth
        


#Twitter Streamer
class TwitterStreamer():
# Class for streaming and processing live tweets

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
        pass

    def stream_tweets(self,fetched_tweets_filename,hash_tag_list):
        #this handles twitter authentication & the connection to the twitter streaming API
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth,listener)

        stream.filter(track=hash_tag_list)


class TwitterListener(StreamListener):
    # Basic listening class that prints received tweets to stdout
    
    def __init__(self,fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self,data):
        try:
            print(data)
            with open(self.fetched_tweets_filename,'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print(f'Error on data: {str(e)}')
        return True

    def on_error(self,status):
        if status == 420:
            # Returning false on data method in case rate limit occurs
            return False
        print(status)
    
    
    

def fetch_user_timeline():
    twitter_client = TwitterClient()
    api = twitter_client.get_twitter_client_api()
    
    tweets = api.user_timeline(screen_name="markets",count=10)
    return tweets

def save_to_db():
    original_tweets = fetch_user_timeline()
    for original_tweet in original_tweets:
        if not original_tweet.retweeted:
            if not Tweet.objects.filter(tweet_id=original_tweet.id):
                new_tweet = Tweet(tweet_id = original_tweet.id, tweet_text = original_tweet.text, published_date = original_tweet.created_at, is_active = True,tweet_likes=original_tweet.favorite_count,tweet_retweets=original_tweet.retweet_count)
                new_tweet.save()  