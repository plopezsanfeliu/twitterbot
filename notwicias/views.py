from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from notwicias.bot import Bot
from notwicias.models import Tweet


def index(request):
    last_tweets = Tweet.objects.filter(category=0).order_by('-twitter_id')[:5]
    return render(request, 'notwicias/index.html', {'last_tweets': last_tweets})


def start_bot(request):
    b = Bot()
    b.loop()

    return HttpResponse("Server running")