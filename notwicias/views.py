from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index():
    return HttpResponse("De moment OK")