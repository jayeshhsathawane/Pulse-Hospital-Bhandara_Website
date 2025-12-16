# pulsehospital/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from .models import Appointment, Doctor # Ensure Appointment model has diagnosis/medication fields
from .forms import AppointmentForm 

# --- STATIC PAGE VIEWS (No change) ---

def home(request):
    return render(request, 'index.html') 

def services(request):
    return render(request, 'services.html')

def doctors(request):
    return render(request, 'doctors.html')

def pharmacy(request):
    return render(request, 'pharmacy.html')

def gallery(request):
    return render(request, 'gallery.html')


# --- DYNAMIC VIEWS ---

def contact(request):
    """
    Handles the Appointment form submission and saves data linked to the chosen Doctor.
    """
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            
            doctor_instance = form.cleaned_data['doctor'] 
            appointment = form.save(commit=False)
            appointment.assigned_doctor = doctor_instance
            appointment.save()
            
            return redirect('pulsehospital:home') 
    else:
        form = AppointmentForm()
        
    return render(request, 'contact.html', {'form': form})


# --- DASHBOARD LOGIC (Updated with Monthly Reporting) ---

def _get_dashboard_context(request):
    """Helper function to fetch common dashboard data (Doctor profile, monthly count)."""
    try:
        doctor = Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        # If user is logged in but not linked to a Doctor profile
        return {'error': True, 'message': 'Error: Your user account is not linked to a Doctor profile.'}

    # Monthly Report Logic (Total Confirmed patients this month)
    current_month = date.today().month
    current_year = date.today().year
    
    # Count appointments CONFIRMED this month for this doctor
    monthly_patient_count = Appointment.objects.filter(
        assigned_doctor=doctor,
        status='Confirmed',
        appointment_date__month=current_month,
        appointment_date__year=current_year
    ).count()
    
    return {
        'doctor': doctor,
        'monthly_patient_count': monthly_patient_count,
        'current_month_name': date.today().strftime('%B')
    }


@login_required(login_url='/accounts/login/')
def doctor_dashboard(request):
    """
    Renders the main dashboard showing ALL future/pending appointments for the logged-in doctor.
    """
    context = _get_dashboard_context(request)
    if 'error' in context:
        return render(request, 'error.html', context)
    
    # Filter all appointments assigned to this specific doctor
    appointments = Appointment.objects.filter(assigned_doctor=context['doctor']).order_by('appointment_date', 'appointment_time')
    context['appointments'] = appointments
    
    return render(request, 'doctor_dashboard.html', context)


@login_required(login_url='/accounts/login/')
def dashboard_today(request):
    """
    Renders the dashboard showing ONLY today's appointments for the logged-in doctor.
    """
    context = _get_dashboard_context(request)
    if 'error' in context:
        return render(request, 'error.html', context)
    
    # Filter appointments for today's date
    today_appointments = Appointment.objects.filter(assigned_doctor=context['doctor'], appointment_date=date.today()).order_by('appointment_time')
    context['appointments'] = today_appointments
    
    return render(request, 'doctor_dashboard.html', context)


# --- PATIENT DETAIL & PRESCRIPTION LOGIC (Updated to Save Data and Change Status) ---

@login_required(login_url='/accounts/login/')
def patient_detail(request, pk):
    """
    Handles saving the prescription, changing appointment status, and rendering the detail view.
    """
    # Fetch the specific appointment, ensuring it belongs to the logged-in doctor
    appointment = get_object_or_404(Appointment, pk=pk, assigned_doctor__user=request.user)
    doctor = appointment.assigned_doctor

    if request.method == 'POST':
        # 1. Capture prescription data from the form
        diagnosis = request.POST.get('diagnosis')
        medication = request.POST.get('medication')
        
        # 2. Save prescription details to the Appointment model
        appointment.diagnosis = diagnosis
        appointment.medication = medication
        
        # 3. VITAL: Change status to 'Confirmed' upon saving the prescription
        appointment.status = 'Confirmed'
        appointment.save()
        
        # Success: Redirect back to the detail page (GET request) to show saved data/allow print
        return redirect('pulsehospital:patient_detail', pk=pk)

    # Context for the GET request (initial render or after POST reload)
    return render(request, 'patient_detail.html', {'appointment': appointment, 'doctor': doctor})