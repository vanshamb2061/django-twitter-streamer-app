from django.contrib import admin
from .models import Tweet,TwitterAccounts

# Register your models here.
admin.site.register(Tweet)
admin.site.register(TwitterAccounts)