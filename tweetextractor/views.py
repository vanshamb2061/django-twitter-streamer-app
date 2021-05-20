from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Tweet
from .algorithms import tweetextraction,userextraction
from . import forms


# Create your views here.
def fetch_tweets(request):
    tweetextraction.save_to_db()
    return redirect('tweetextractor:tweet_list')

def tweet_list(request):
    tweets = Tweet.objects.order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(tweets, 10)
    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)
    return render(request, 'tweetextractor/tweet_list.html', {'tweets': tweets})



# @login_required(login_url = '/accounts/login')
def addaccount(request):
    if request.method == "POST":
        form = forms.AddAccount(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
        # if form.is_valid():
        #     userextraction.add_account(form['screen_name'])
        return redirect('tweetextractor:tweet_list')
    else:
        form = forms.AddAccountForm
        return render(request,'tweetextractor/add_user.html',{'form':form})