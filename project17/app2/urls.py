# app2/urls.py
from django.urls import path
from app2.views import *
app_view="app2"
urlpatterns = [
    path('page1/', page1, name='app2_page1'),
    path('page2/', page2, name='app2_page2'),
]