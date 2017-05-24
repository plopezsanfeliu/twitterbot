from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from notwicias.bot import Bot


def index(request):
    return HttpResponse("Index of Notwicias")


def start_bot(request):
    b = Bot()
    b.loop()

    return HttpResponse("Server running")


def stop_bot(request):
    b = Bot()
    b.loop = False

    return HttpResponse("Server stopped")