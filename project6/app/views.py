from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def krishnaa(request):
    return HttpResponse("krishna pathi")
def krishnacho(request):
    return render(request,"krishnacho.html")