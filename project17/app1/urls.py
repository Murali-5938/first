
from django.urls import path
from app1.views import *
app_view="app1"

urlpatterns = [
    path('page1/', page1, name='app1_page1'),
    path('page2/', page2, name='app1_page2'),
]