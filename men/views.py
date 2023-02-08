from django.shortcuts import render

# Create your views here.
from urllib import request
from django.http import HttpResponse



def index(request):
    return render(request, 'men/index.html')