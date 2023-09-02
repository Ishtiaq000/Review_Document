from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Review_Doc_backend.urls')),  # Include app-specific URLs
]
