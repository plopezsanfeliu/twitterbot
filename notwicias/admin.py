from django.contrib import admin

# Register your models here.
from models import Tweet, TwitterUser, UserRelation

admin.site.register(Tweet)
admin.site.register(TwitterUser)
admin.site.register(UserRelation)