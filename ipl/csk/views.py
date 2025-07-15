from django.shortcuts import render
from django.http import HttpResponse

def captain(request):
    return HttpResponse("<h1>ruthuraj is  best batsmen</h1>")
def viceCaptain(request):
    return HttpResponse("<h2>R jadeja is a good allrounder</h2>")