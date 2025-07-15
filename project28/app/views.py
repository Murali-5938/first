from django.shortcuts import render
from django.views.generic import ListView
from app.models import *
# Create your views here.
class StudentList(ListView):
    model=Student
    template_name='StudentList.html'
    context_object_name='students'
    ordering=['sname']
    queryset=Student.objects.filter(sname='nani')    