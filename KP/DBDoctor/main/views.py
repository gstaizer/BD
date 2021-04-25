from django.shortcuts import render, redirect
from .models import User1, Notification, Hospital, Review, Doctor, Appointment
from .forms import AppointmentForm, UserForm, AvatarForm
from django.http import HttpResponseRedirect, HttpResponseNotFound


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, "main/index.html", {'title': 'Главная страница'})

def about(request):
    return render(request, "main/about.html", {'title': 'О нас'})

def appointments(request):
    return render(request, "main/crate-account.html")

def createappointment(request):
    if request.user.is_authenticated:
        users = User1.objects.all()
        users_auth_bool = False
        if not (str(request.user) == "AnonymousUser"):
            for user in users:
                if (str(user.id_registarion) == str(request.user.id)):
                    users_auth_bool = True
                    break
            if users_auth_bool == False:
                return redirect('createacc')
        if not (str(request.user) == 'AnonymousUser'):
            error = ''
            if request.method == 'POST':
                form = AppointmentForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.id_user = user.objects.get(id_registarion=request.user.id)
                    post.id_doctor = Doctor.objects.get(name=request.POST.get("id_doctor"))
                    post.time_to_appointment = Appointment.objects.get(name=request.POST.get("time_to_appointment"))
                    post.save()
                    return redirect('appointments')
                else:
                    error = 'Форма неверная'
        form = AppointmentForm()
        context = {
            'form': form,
            'error': error,
        }

        return render(request, "main/create-appointment.html", context)
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

def createacc(request):
    error = ''
    User1.objects.filter(id_registarion=request.user.id).delete()
    if not (str(request.user) == 'AnonymousUser'):
        if request.method == 'POST':
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.id_registarion = request.user.id
                post.save()
                return redirect('/')
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
        appointments = Appointment.objects.all()
        self_user = User1.objects.get(id_registarion = request.user.id)
        user_info = str(request.user)

        return render(request, 'main/profile.html', {'title': 'Профиль', 'self_user': self_user, 'user_info':user_info})
    except ValueError:
        return redirect('createacc')
    except UnboundLocalError:
        return redirect('createacc')

def id_up_status(request, cancel = False):
    if not (str(request.user) == 'AnonymousUser'):
        users = User1.objects.all()

        users = False
        for user in users:
            if (str(user.id_registarion) == str(request.user.id)):
                users_auth_bool = True
                break
        if users_auth_bool == False:
            return redirect('createacc')

    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

    return redirect('appointments')

def edit_avatar(request):
    error = ''
    temp_user = User1.objects.get(id_registarion=request.user.id)
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            temp_user.avatar = user.avatar
            temp_user.save()
            return redirect('/')
        else:
            error = 'Форма неверная'

    form = UserForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/edit-avatar.html', context)

def edit_data(request):
    try:
        user = User1.objects.get(id_registarion=request.user.id)
        if request.method == "POST":
            user.name = request.POST.get("name")
            user.surname = request.POST.get("surname")
            user.save()
            return HttpResponseRedirect("/profile")
        else:
            return render(request, "main/edit-data.html", {'title': 'Редактирование профиля', "user": user})
    except user.DoesNotExist:
        return HttpResponseNotFound("<h2>Human not found</h2>")

def id_down_status(request):
    if not (str(request.user) == 'AnonymousUser'):
        users = User1.objects.all()

        users_auth_bool = False
        for user in users:
            if (str(user.id_registarion) == str(request.user.id)):
                users_auth_bool = True
                break
        if users_auth_bool == False:
            return redirect('createacc')

    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

    return redirect('appointments')


def appointment_list(request):
    hospitals = Hospital.objects.all()
    return render(request, "main/index.html", {'title': 'Главная страница', 'hospitals': hospitals})