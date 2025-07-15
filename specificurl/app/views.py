from django.shortcuts import render

from django.http import HttpResponse

def function1(request):
    return HttpResponse("This is function1 view")

