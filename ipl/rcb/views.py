from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def captain(request):
    return HttpResponse("<h1>virat is world best batsmen </h1>")
def viceCaptain(request):
    return HttpResponse("<h1>patidhar is ranji best batsmen </h1>")