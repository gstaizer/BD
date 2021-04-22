from django.shortcuts import render, redirect
from .models import User, Notification, Hospital, Review, Doctor, Appointment
from .forms import AppointmentForm


def index(request):
    hospitals = Hospital.objects.all()
    return render(request, "main/index.html", {'title': 'Главная страница', 'hospitals': hospitals})

def about(request):
    return render(request, "main/about.html", {'title': 'О нас'})

def create(request):
    error = ''
    users = User.objects.all()
    doctors = Doctor.objects.all()
    reviews = Review.objects.all()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "ERROR форма не корректна"

    form = AppointmentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "main/create-appointment.html", {'title': 'Запись на прием', 'users': users, 'doctors': doctors, 'reviews': reviews})



def appointment_list(request):
    hospitals = Hospital.objects.all()
    return render(request, "main/index.html", {'title': 'Главная страница', 'hospitals': hospitals})