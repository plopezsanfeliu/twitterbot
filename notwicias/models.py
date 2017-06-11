from django.conf import settings
from django.db import models


# Create your models here.
class Tweet(models.Model):
    twitter_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=25)
    user = models.CharField(max_length=25)
    language = models.CharField(max_length=4)
    retweets = models.IntegerField()
    favorites = models.IntegerField()
    coordinates = models.CharField(max_length=50, null=True)
    text = models.CharField(max_length=160)
    date = models.DateField()
    time = models.TimeField()
    category = models.SmallIntegerField()

    def __unicode__(self):
        return "Twitter ID: {}; Text: {}".format(self.twitter_id, self.text.encode('ascii', 'ignore').decode('ascii'))


class TwitterUser(models.Model):
    name = models.CharField(max_length=15, unique=True)
    valid = models.BooleanField()

    def __str__(self):
        return self.name


class UserRelation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ", " + str(self.group)
