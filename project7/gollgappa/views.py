from django.shortcuts import render
from django.http import HttpResponse

def panipuri(request):
    return render(request,'panipuri.html')
def dhaipuri(request):
    return HttpResponse("<h1>dhaipuri </h1>")