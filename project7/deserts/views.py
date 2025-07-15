from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def apricot(request):
    return render(request,"apricot.html")
def gulabjamn(request):
    return HttpResponse("<h1>gulabjamn is so sweet </h1>")