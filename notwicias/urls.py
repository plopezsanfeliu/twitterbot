from django.conf.urls import url

from notwicias import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bot/start', views.start_bot, name='start_bot'),
]