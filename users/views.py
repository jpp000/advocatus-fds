from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(req):
    return render(req, 'register.html')


def login(req):
    return render(req, 'login.html')