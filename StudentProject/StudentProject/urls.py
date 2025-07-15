from django.contrib import admin
from django.urls import path
from StudentApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.student_registration, name='register'),
]
