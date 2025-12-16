# pulsehospital/models.py
from django.db import models
from django.contrib.auth.models import User

# Department Choices MUST be defined here for the model field
DEPARTMENT_CHOICES = [
    ('general-medicine', 'General Medicine'),
    ('cardiology', 'Cardiology'),
    ('diabetes', 'Diabetes Care'),
    ('gynecology', 'Gynecology & Obstetrics'),
    ('maternity', 'Maternity Care'),
    ('pharmacy', 'Pharmacy'),
]

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)     
    medication = models.TextField(blank=True, null=True)    
    # VITAL: Choices defined directly on the model field
    department = models.CharField(
        max_length=100,
        choices=DEPARTMENT_CHOICES,
        default='general-medicine'
    )
    
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) 
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField(blank=True)
    booked_on = models.DateTimeField(auto_now_add=True)
    
    status = models.CharField(
        max_length=20,
        default='Pending',
        choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')]
    )

    def __str__(self):
        return f"{self.patient_name} - {self.assigned_doctor.name}"