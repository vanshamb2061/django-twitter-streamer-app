from django import forms
from .models import TwitterAccounts


class AddAccount(forms.ModelForm):
    class Meta:
        model = TwitterAccounts
        fields = ['twitter_user_id','twitter_name','twitter_screen_name','twitter_location']