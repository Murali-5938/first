from django.urls import path
from . import views

app_name = 'app'  # important for namespacing

urlpatterns = [
    path('function1/', views.function1, name='function1'),
]
