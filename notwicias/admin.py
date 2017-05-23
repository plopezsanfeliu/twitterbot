from django.contrib import admin

# Register your models here.
from models import Tweet, TwitterUser, User

admin.site.register(Tweet)
admin.site.register(TwitterUser)
admin.site.register(User)