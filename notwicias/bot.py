from django.db import IntegrityError
from time import sleep

import tweepy

from notwicias.models import TwitterUser, Tweet


def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance


@singleton
class Bot():
    def __init__(self):
        self.__consumer_key = "cNbkKHve3645xLIVgJjQbrWg6"
        self.__consumer_secret = "B1SWKCIMFQjhh3Y5YGstKMvl8t7IAPTha1jxXy5b3IC6K8wz7w"
        self.__access_token = "3720533727-cBbDc2bDnDSU6f9SuC3ti4oQcfTkMk7VbVmh9ZW"
        self.__access_token_secret = "k2aioMNx3tCfw6jW9teksQ98WllWbKogVQF4YW0sRYTuW"

        auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret)
        auth.set_access_token(self.__access_token, self.__access_token_secret)

        self.__api = tweepy.API(auth)

    def getTweetsByName(self, name, number):
        tweet_list = []

        tweets = self.__api.user_timeline(screen_name=name, count=number)

        for status in tweets:
            tweet_info = [status.id, status.author.screen_name, status.author.name, status.lang, status.retweet_count,
                          status.favorite_count, status.coordinates, status.text.replace('"', "\""),
                          status.created_at.strftime('%Y-%m-%d'), status.created_at.strftime('%H:%m:%S')]
            tweet_list.append(tweet_info)

        return tweet_list

    def addTweets(self, tweet_list):
        for tweet_info in tweet_list:
            u = Tweet(twitter_id=tweet_info[0], username=tweet_info[1], user=tweet_info[2], language=tweet_info[3],
                      retweets=tweet_info[4], favorites=tweet_info[5], coordinates=tweet_info[6], text=tweet_info[7],
                      date=tweet_info[8], time=tweet_info[9], category=0)
            try:
                u.save()
            except IntegrityError:
                pass

    def loop(self):
        while True:
            user_list = TwitterUser.objects.all()
            tweets = []

            for user in user_list:
                tweets += self.getTweetsByName(user.name, 20)

            self.addTweets(tweets)
            sleep(300)
