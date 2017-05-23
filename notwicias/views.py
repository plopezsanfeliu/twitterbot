from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import tweepy

from notwicias.models import TwitterUser, Tweet


def index(request):
    return HttpResponse("Index of Notwicias")


def getTweetsByName(api, name, number):
    tweet_list = []

    tweets = api.user_timeline(screen_name=name, count=number)

    for status in tweets:
        tweet_info = [status.id, status.author.screen_name, status.author.name, status.lang, status.retweet_count,
                      status.favorite_count, status.coordinates, status.text.replace('"', "\""),
                      status.created_at.strftime("%Y/%m/%d"), status.created_at.strftime("%H:%m:%S")]
        tweet_list.append(tweet_info)

    return tweet_list


def addTweets(tweet_list):
    error = 0
    for tweet_info in tweet_list:
        query = (
            """INSERT INTO tweet (id, username, user, language, retweets, favorites, coordinates, text, date, time, 
        category) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', "%s", '%s', '%s', '%s') ON DUPLICATE KEY UPDATE 
        retweets = %s, favorites = %s;""" %
            (tweet_info[0], tweet_info[1], tweet_info[2], tweet_info[3],
             tweet_info[4], tweet_info[5], tweet_info[6],
             tweet_info[7].replace(u'\u2019', u'\'').
             replace(u'\u2026', u'...').replace(u'\u2018', u'\'').
             replace(u'\u25b6', u'[PLAY]').replace(u'\u201c', u'\"').
             replace(u'\u201d', u'\'').replace('"', '\'').
             replace(u'\u2013', '-').replace(u'\u20ac', 'EUR').
             replace(u'\uf006', '-').replace(u'\u2014', '-'),
             tweet_info[8], tweet_info[9], "0", tweet_info[4], tweet_info[5]))
        u = Tweet(twitter_id=tweet_info[0], username=tweet_info[1], user=tweet_info[2], language=tweet_info[3],
                        retweets=tweet_info[4], favorites=tweet_info[5], coordinates=tweet_info[6], text=tweet_info[7],
                        date=tweet_info[8].replace("/", "-"), time=tweet_info[9], category=0)

        u.save()


def bot(request):
    consumer_key = "cNbkKHve3645xLIVgJjQbrWg6"
    consumer_secret = "B1SWKCIMFQjhh3Y5YGstKMvl8t7IAPTha1jxXy5b3IC6K8wz7w"
    access_token = "3720533727-cBbDc2bDnDSU6f9SuC3ti4oQcfTkMk7VbVmh9ZW"
    access_token_secret = "k2aioMNx3tCfw6jW9teksQ98WllWbKogVQF4YW0sRYTuW"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    user_list = TwitterUser.objects.all()
    tweets = []

    for user in user_list:
        tweets += getTweetsByName(api, user.name, 2)

    addTweets(tweets)

    return HttpResponse(tweets)
