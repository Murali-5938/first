from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from app.models import *
def display_topic(request):
    TL=Topic.objects.all()
    d={'TL':TL}
    return render(request,'display_topic.html',d)
def display_webpage(request):
    WPTL=WebPage.objects.all()
    d={'WPTL':WPTL}
    return render(request,'display_webpage.html',d)
def display_arecords(request):
    ARTL=AccessRecords.objects.all()
    d={'ARTL':ARTL}
    return render(request,'display_arecords.html',d)
def insert_topic(request):
    tn=input('enter the topic')
    TTO=Topic.objects.get_or_create(topic_name=tn)
    if TTO[1]:
        TL=Topic.objects.all()
        d={'TL':TL}
        return render(request,'display_topic.html',d)
    else:
        return render(request,'display_topic.html')
def insert_webpage(request):
    tn=input('enter the topic')
    LTO=Topic.objects.get(topic_name=tn)
    if LTO:
        na=input("name ")
        url=input("url ")
        em=input('email ')
        Two=WebPage.objects.get_or_create(topic_name=LTO,name=na,url=url,email=em)
        if Two[1]:
             WPTL=WebPage.objects.all()
             d={'WPTL':WPTL}
             return render(request,'display_webpage.html',d)
        else:
            return render(request,'display_webpage.html')


def access_record(request):
    pk=input('enter the id of webpage')
    wo=WebPage.objects.filter(pk=pk)
    date=input("enter the date")
    author=input("enter the author name")
    TAO=AccessRecords.objects.get_or_create(name=wo,date=date,author=author)
    if TAO[1]:
        ARTL=AccessRecords.objects.all()
        d={'ARTL':ARTL}
        return render(request,'display_arecords.html',d)
    else:
        return render(request,'display_arecords.html')
def update_topic(request):
    #WebPage.objects.filter(name='mural').update(url='http://mural.in')
    WebPage.objects.filter(name='krishna').update(url='http://krishna.in')

    
    WPTL=WebPage.objects.all()

    d={'WPTL':WPTL}
    return render(request,'display_webpage.html',d)
def delete_topic(request):
    #WebPage.objects.filter(name='mural').update(url='http://mural.in')
    #WebPage.objects.filter(name='krishna').update(url='http://krishna.in')

    #WebPage.objects.filter(name='mural').delete()
    #FO=Topic.objects.get(topic_name='cricket')
    #WebPage.objects.update_or_create(name='Murali2',defaults={'topic_name':FO})
    WebPage.objects.filter(name='Murali2').delete()

    WebPage.objects.filter(name='Murali2').update(url='http://murali2.in')

    
    WPTL=WebPage.objects.all()

    d={'WPTL':WPTL}
    return render(request,'display_webpage.html',d)
