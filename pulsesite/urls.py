"""
URL configuration for pulsesite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# pulsesite/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include the pulsehospital URLs at the project root level
    # e.g., A request to '/' goes to pulsehospital.urls
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('pulsehospital.urls')), 
]

# IMPORTANT: Serve static files during development
if settings.DEBUG:
    # This configuration is crucial for Django to serve files from the 
    # global 'static' folder when DEBUG is True (during development).
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
