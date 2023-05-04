from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from .models import Person
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_password = request.POST['password']
        if Person.objects.filter(email=email).exists():
            obj=Person.objects.get(email=email)
            password=obj.password
            if check_password(user_password,password):
                return redirect('/welcome/')
            else:
                return HttpResponse('password incorect')
def welcome(request):
    return (re)

def registration(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if Person.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        else:
            Person.objects.create(name=name, email=email, password=password)
        return redirect('/')
    else:
        return HttpResponse('Email is not register')
