from django.db import models


# Create your models here.
class Tweet(models.Model):
    twitter_id = models.BigIntegerField()
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
    name = models.CharField(max_length=15)
    valid = models.BinaryField()


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    admin = models.BinaryField()


class UserRelations(models.Model):
    user = models.ForeignKey(User)
    group = models.CharField(max_length=15)