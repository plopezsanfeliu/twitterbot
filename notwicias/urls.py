from django.conf.urls import url

from notwicias import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bot/start', views.start_bot, name='start_bot'),
    url(r'^category/(?P<category_id>[0-9]{1})/$', views.category, name='category'),
    url(r'^signin', views.sign_in, name='sign_in'),
    url(r'^login', views.log_in, name='log_in'),
    url(r'^logout', views.log_out, name='log_out'),
    url(r'^most/(?P<type>[\w-]+)/$', views.most, name='most'),
    url(r'^manage', views.manage, name='manage'),
    url(r'^modify/(?P<group_id>[0-9]{1})/$', views.modify, name='modify'),
]
