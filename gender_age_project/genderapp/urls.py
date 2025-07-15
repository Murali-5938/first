from django.urls import path
from genderapp.views import *

urlpatterns = [
    path('index/', index, name='index'),  # Changed from 'index' to ''
]
