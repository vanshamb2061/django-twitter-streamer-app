# Generated by Django 3.2.3 on 2021-05-19 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetextractor', '0010_rename_tweet_hashtags_tweet_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='tags',
            new_name='tweet_hashtags',
        ),
    ]
