from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import tweepy

from notwicias.models import TwitterUser


def index(request):
    consumer_key = "cNbkKHve3645xLIVgJjQbrWg6"
    consumer_secret = "B1SWKCIMFQjhh3Y5YGstKMvl8t7IAPTha1jxXy5b3IC6K8wz7w"
    access_token = "3720533727-cBbDc2bDnDSU6f9SuC3ti4oQcfTkMk7VbVmh9ZW"
    access_token_secret = "k2aioMNx3tCfw6jW9teksQ98WllWbKogVQF4YW0sRYTuW"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    userList = TwitterUser.objects.first()

    str = ""

    for user in userList:
        str += user.name

    return HttpResponse(str)