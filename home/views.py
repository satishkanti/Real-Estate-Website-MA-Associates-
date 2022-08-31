from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def index(request):
    return render(request,'index.html')
