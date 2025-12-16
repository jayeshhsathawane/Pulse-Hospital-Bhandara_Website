
# pulsehospital/admin.py
from django.contrib import admin
from .models import Doctor, Appointment

# Doctor Model
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'user') # Admin list view में ये फील्ड दिखेंगी
    search_fields = ('name', 'specialty')
    
# Appointment Model 
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    # Admin list 
    list_display = ('patient_name', 'assigned_doctor', 'appointment_date', 'status', 'booked_on')
    # Filter options
    list_filter = ('status', 'assigned_doctor', 'department')
    search_fields = ('patient_name', 'phone', 'reason')