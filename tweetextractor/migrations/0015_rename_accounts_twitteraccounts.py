# Generated by Django 3.2.3 on 2021-05-20 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetextractor', '0014_tweet_is_retweeted'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Accounts',
            new_name='TwitterAccounts',
        ),
    ]
