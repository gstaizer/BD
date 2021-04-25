from django.shortcuts import render, redirect
from .models import User1, Notification, Hospital, Review, Doctor, Appointment
from .forms import AppointmentForm, UserForm
from django.http import HttpResponseRedirect, HttpResponseNotFound


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    hospitals = Hospital.objects.all()
    return render(request, "main/index.html", {'title': 'Главная страница', 'hospitals': hospitals})

def about(request):
    return render(request, "main/about.html", {'title': 'О нас'})

def createappointment(request):
    error = ''
    self_user = User1.objects.get(id_registarion=request.user.id)
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
    return render(request, "main/create-appointment.html", {'title': 'Запись на прием', 'self_user': self_user, 'doctors': doctors, 'reviews': reviews})

def createaccount(request):
    error = ''

    User1.objects.filter(id_registarion=request.user.id).delete()
    if not (str(request.user) == 'AnonymousUser'):
        if request.method == 'POST':
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.id_registarion = request.user.id
                post.save()
            else:
                error = 'Форма неверная'

        form = UserForm()
        context = {
            'form': form,
            'error': error,
        }
        return render(request, 'main/create-account.html', context)

def profile(request):
    try:

        self_user = User1.objects.get(id_registarion = request.user.id)
        user_info = str(request.user)

        return render(request, 'main/profile.html', {'title': 'Профиль', 'self_user': self_user, 'user_info':user_info})
    except ValueError:
        return redirect('main/create-account')
    except UnboundLocalError:
        return redirect('main/create-account')

def id_up_status(request, cancel = False):
    if not (str(request.user) == 'AnonymousUser'):
        users = User1.objects.all()

        users = False
        for user in users:
            if (str(user.id_registarion) == str(request.user.id)):
                users_auth_bool = True
                break
        if users_auth_bool == False:
            return redirect('main/create-account')

    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

    return redirect('/')


def id_down_status(request):
    if not (str(request.user) == 'AnonymousUser'):
        users = User1.objects.all()

        users_auth_bool = False
        for user in users:
            if (str(user.id_registarion) == str(request.user.id)):
                users_auth_bool = True
                break
        if users_auth_bool == False:
            return redirect('main/create-account')

    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

    return redirect('main/tasks')


def appointment_list(request):
    hospitals = Hospital.objects.all()
    return render(request, "main/index.html", {'title': 'Главная страница', 'hospitals': hospitals})