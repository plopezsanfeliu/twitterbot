from django.conf.urls import url

from notwicias import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]