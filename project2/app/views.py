from django.shortcuts import render
from django.http import HttpResponse
def murali(request):
    return HttpResponse("murali chowdary pathi is job seeker")
def pathi(request):
    return HttpResponse("pathi murali chowdary waiting for best moment")
def krishna(request):
    return HttpResponse("<h1>krishna is waiting for his sathyabhama</h1>")
def jagan(request):
    return HttpResponse('<h1>jayakumar is waiting for his anupuma</h1>') 