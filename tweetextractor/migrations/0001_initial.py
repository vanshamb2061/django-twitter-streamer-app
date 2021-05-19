# Generated by Django 3.1.5 on 2021-05-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.CharField(blank=True, max_length=250, null=True)),
                ('tweet_text', models.TextField()),
                ('tweet_len', models.IntegerField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('tweet_likes', models.IntegerField()),
                ('tweet_retweets', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
