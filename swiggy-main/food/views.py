from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def biriyani(request):
    return HttpResponse('Tastes of The Biriyani will get spiced up with Beer')

def iceCream(request):
    return HttpResponse('Amulya Likes To Amul Icecreams becoz she is Amul Baby')
