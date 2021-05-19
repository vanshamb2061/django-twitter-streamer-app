from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Tweet(models.Model):
    tweet_id = models.CharField(max_length=250, null=True, blank=True)
    tweet_text = models.TextField()
    tweet_cleaned_text = models.TextField(default="text")
    published_date = models.DateTimeField(blank=True, null=True)
    tweet_likes = models.IntegerField()
    tweet_retweets = models.IntegerField()
    tweet_hashtags = TaggableManager()
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.tweet_text

        
