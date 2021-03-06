from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def login(request):
    return render(request, "login.html")
