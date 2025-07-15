from django.shortcuts import render
from django.views.generic import ListView,DeleteView
from app.models import *
# Create your views here.
class SchoolList(ListView):
    model=School
    context_object_name='scobj'
class SchoolDetail(DeleteView):
    model=School
    context_object_name="scobject"