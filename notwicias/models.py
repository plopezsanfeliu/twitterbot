from django.db import models


# Create your models here.
class Tweet(models.Model):
    twitter_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=25)
    user = models.CharField(max_length=25)
    language = models.CharField(max_length=4)
    retweets = models.IntegerField()
    favorites = models.IntegerField()
    coordinates = models.CharField(max_length=50)
    text = models.CharField(max_length=160)
    date = models.DateField()
    time = models.TimeField()
    category = models.SmallIntegerField()


class TwitterUser(models.Model):
    name = models.CharField(max_length=15, unique=True)
    valid = models.BooleanField()


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=60)
    email = models.CharField(max_length=50, unique=True)
    admin = models.BooleanField()


class UserRelations(models.Model):
    user = models.ForeignKey(User)
    group = models.CharField(max_length=15)