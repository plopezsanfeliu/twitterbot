from django.conf.urls import url

from notwicias import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bot/start', views.start_bot, name='start_bot'),
    url(r'^bot/stop', views.stop_bot, name='stop_bot'),
]