from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def insert_student(request):
    ESTMFO=StudentModelForm()
    d={'ESTMFO':ESTMFO}

    if request.method=="POST":
        STMFDO=StudentModelForm(request.POST)
        if STMFDO.is_valid():
            STMFDO.save()
            return HttpResponse('data is created')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'insert_student.html',d)