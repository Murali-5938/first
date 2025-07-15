from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy

class SchoolList(ListView):
    model=School
    context_object_name='schoolobjects'

class SchoolDetail(DetailView):
    model=School
    context_object_name='scobject'
class SchoolCreate(CreateView):
    model=School
    fields='__all__'
class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'
class SchoolDelete(DeleteView):
    model=School
    success_url=reverse_lazy('SchoolList')





