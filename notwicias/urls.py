from django.conf.urls import url, include

from notwicias import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bot/', views.bot, name='bot'),
]