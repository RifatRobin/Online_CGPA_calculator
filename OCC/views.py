from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def signin(request):
    return render(request, "signin.html")


def signup(request):
    return render(request, 'signup.html')


def calculate(request):
    return render(request, 'calculate.html')
