from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('genderapp.urls')),  # Changed from 'app' to ''
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

