from django.shortcuts import render
from django.http import HttpResponse
def chickenbiryani(request):
    return HttpResponse("<h1>chicken biryani is so good</h1>")
def muttonbirayani(request):
    return render(request,'muttonbirayani.html')