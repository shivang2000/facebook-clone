from django.shortcuts import render
from django.http import HttpResponse , request

def login(request):
    return HttpResponse("login page")