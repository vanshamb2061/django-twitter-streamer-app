# Generated by Django 3.2.3 on 2021-05-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetextractor', '0008_tweet_tweet_cleaned_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet_cleaned_text',
            field=models.TextField(default='text'),
        ),
    ]