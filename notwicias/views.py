# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from notwicias.bot import Bot
from notwicias.forms import SignInForm
from notwicias.models import Tweet
from django.contrib.auth.models import User


def index(request):
    LAST_NUM = 5
    last_tweets_c0 = Tweet.objects.filter(category=0).order_by('-twitter_id')[:LAST_NUM]
    last_tweets_c1 = Tweet.objects.filter(category=1).order_by('-twitter_id')[:LAST_NUM]
    last_tweets_c2 = Tweet.objects.filter(category=2).order_by('-twitter_id')[:LAST_NUM]
    last_tweets_c3 = Tweet.objects.filter(category=3).order_by('-twitter_id')[:LAST_NUM]
    last_tweets_c4 = Tweet.objects.filter(category=4).order_by('-twitter_id')[:LAST_NUM]

    context = {'last_tweets_c0': last_tweets_c0, 'last_tweets_c1': last_tweets_c1, 'last_tweets_c2': last_tweets_c2,
               'last_tweets_c3': last_tweets_c3, 'last_tweets_c4': last_tweets_c4}
    return render(request, 'notwicias/index.html', context)


def category(request, category_id):
    category_set = Tweet.objects.filter(category=category_id).order_by('-twitter_id')[:5]
    return render(request, 'notwicias/category.html', {'category_set': category_set, 'category_id': category_id})


def start_bot(request):
    b = Bot()
    b.loop()
    return HttpResponse("Server running")


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            if data['password1'] == data['password2']:
                try:
                    User.objects.create_user(data['username'], data['email'], data['password1'])
                    return HttpResponse('OK')
                except IntegrityError:
                    return HttpResponse('El nombre de usuario ya existe.')
            else:
                return HttpResponse('Los passwords no coinciden.')
        else:
            return HttpResponse('No se cumplen los requisitos de campos.')
    else:
        form = SignInForm()
        return render(request, 'notwicias/signin.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = request.POST
        user = authenticate(username=form['username'], password=form['password'])
        if user is not None:
            request.session['username'] = form['username']
            return redirect('/notwicias')
        else:
            return HttpResponse('Autenticación fallida.')
    else:
        return HttpResponse('Petición incorrecta')


def log_out(request):
    request.session.flush()
    return redirect('/notwicias')


def most(request, type):
    MAX_TWEETS = 5
    if type == 'favorites':
        type = 'Favoritos'
        tweet_list = Tweet.objects.order_by('-favorites')[:MAX_TWEETS]
    elif type == 'retweets':
        type = 'Retuiteados'
        tweet_list = Tweet.objects.order_by('-retweets')[:MAX_TWEETS]
    return render(request, 'notwicias/most.html', {'type': type, 'tweet_list': tweet_list})