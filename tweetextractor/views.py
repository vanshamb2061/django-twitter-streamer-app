from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Tweet
from .twitter import save_to_db


# Create your views here.

def tweet_fetch(request):
    save_to_db()
    return redirect('tweet_list')

# @login_required
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
