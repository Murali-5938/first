from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def djforms(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFOWD=StudentForm(request.POST)
        if SFOWD.is_valid():
            return HttpResponse(str(SFOWD.cleaned_data))

    return render(request,'djforms.html',d)



