
# pulsehospital/urls.py
from django.urls import path, include  
from . import views

# ADD THIS LINE to define the namespace for your app
app_name = 'pulsehospital'

urlpatterns = [
    # The URL name is 'home', mapped to the views.home function.
    path('', views.home, name='home'),
    
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
   # Doctor Dashboard & Detail Views
    path('dashboard/', views.doctor_dashboard, name='dashboard'),
    path('dashboard/today/', views.dashboard_today, name='dashboard_today'), # New Today's Appt.
    path('dashboard/patient/<int:pk>/', views.patient_detail, name='patient_detail'), # Prescription Page
    
]