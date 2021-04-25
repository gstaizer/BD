from django.shortcuts import render, redirect
from .models import User1, Notification, Hospital, Review, Doctor, Appointment
from .forms import AppointmentForm, UserForm, AvatarForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from datetime import datetime
from django.db.models import Q


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, "main/index.html", {'title': 'Главная страница'})

def about(request):
    return render(request, "main/about.html", {'title': 'О нас'})


def appointments(request, order_like='name'):
    if request.user.is_authenticated:
        search_query = request.GET.get('search', '')
        order_like = request.GET.get('order_like', '')
        appointment_list = Appointment.objects.all()

        try:
            if search_query:
                appointment_list = Appointment.objects.filter(id_doctor__icontains = search_query)
            else:
                appointment_list = Appointment.objects.all()
        except ValueError:
            appointment_list = []

        if order_like:
            appointment_list = appointment_list.order_by(order_like)

        if not (str(request.user) == "AnonymousUser"):
            if str(User1.objects.filter(id_registarion=request.user.id)) == "<QuerySet []>":
                return redirect('createacc')

        self_user = User1.objects.get(id_registarion=request.user.id)
        app_user = Appointment.objects.filter(id_user = self_user)

        list_to_view = []
        for el in appointment_list:
            #self_app_user = Appointment.objects.filter(id_user = el.id_user)
           # if app_user == self_app_user:
                list_to_view.append(el.id)

        paginator = Paginator(appointment_list, 5)

        page = request.GET.get('page')
        try:
            appointments = paginator.page(page)
        except PageNotAnInteger:
            appointments = paginator.page(1)
        except EmptyPage:
            appointments = paginator.page(paginator.num_pages)

        user_info = str(request.user)
        return render(request, 'main/appointments.html',
                      {'title': 'Записи на прием', 'appointments': appointments, 'user_info': user_info, 'list_to_view': list_to_view})
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

def notifications(request):
    if request.user.is_authenticated:

        search_query = request.GET.get('search', '')
        order_like = request.GET.get('order_like', '')

        try:
            if search_query:
                notifications_list = Notification.objects.filter(notification_text__icontains = search_query)
            else:
                notifications_list = Notification.objects.all()
        except ValueError:
            notifications_list = []

        if order_like:
            notifications_list = notifications_list.order_by(order_like)

        if not (str(request.user) == "AnonymousUser"):
            if str(User1.objects.filter(id_registarion=request.user.id)) == "<QuerySet []>":
                return redirect('createacc')

        list_to_view = []
        for el in notifications_list:
                list_to_view.append(el.id)

        paginator = Paginator(notifications_list, 10)

        page = request.GET.get('page')
        try:
            notifications = paginator.page(page)
        except PageNotAnInteger:
            notifications = paginator.page(1)
        except EmptyPage:
            notifications = paginator.page(paginator.num_pages)

        user_info = str(request.user)
        return render(request, 'main/notifications.html',
                      {'title': 'Ваши Уведомления', 'notifications': notifications, 'user_info': user_info, 'list_to_view': list_to_view})
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

def doctors(request, order_like='full_name'):
    if request.user.is_authenticated:
        search_query = request.GET.get('search', '')
        order_like = request.GET.get('order_like', '')

        try:
            if search_query:
                doctors_list = Doctor.objects.filter(full_name__icontains=search_query)
            else:
                doctors_list = Doctor.objects.all()
        except ValueError:
            doctors_list = []

        if order_like:
            doctors_list = doctors_list.order_by(order_like)

        if not (str(request.user) == "AnonymousUser"):
            if str(User1.objects.filter(id_registarion=request.user.id)) == "<QuerySet []>":
                return redirect('createacc')

        list_to_view = []
        for el in doctors_list:
            # self_app_user = Appointment.objects.filter(id_user = el.id_user)
            # if app_user == self_app_user:
            list_to_view.append(el.id)

        paginator = Paginator(doctors_list, 10)

        page = request.GET.get('page')
        try:
            doctors = paginator.page(page)
        except PageNotAnInteger:
            doctors = paginator.page(1)
        except EmptyPage:
            doctors = paginator.page(paginator.num_pages)

        user_info = str(request.user)
        return render(request, 'main/doctors.html',
                      {'title': 'Наши врачи', 'doctors': doctors, 'user_info': user_info, 'list_to_view': list_to_view})
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

def createappointment(request):
    if request.user.is_authenticated:
        users = User1.objects.all()
        doctors = Doctor.objects.all()
        reviews = Review.objects.all()
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
                    post.id_user = User1.objects.get(id_registarion = request.user.id)
                    post.id_doctor = request.POST.get("id_doctor")
                    post.time_to_appointment = request.POST.get("time_to_appointment")
                    post.id_review = reviews[0]
                    nower = datetime.now()
                    post.name = "Регистрация посещения: " + nower.strftime('%d/%m/%Y')
                    post.save()
                    return redirect('appointments')
                else:
                    error = 'Форма неверная'
        form = AppointmentForm()
        context = {
            'form': form,
            'error': error,
        }

        return render(request, "main/create-appointment.html", {'title': 'Редактирование профиля', 'context': context, 'doctors': doctors})
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

def delete_appointment(request, id):
    appointment = Appointment.objects.get(pk=id)
    appointment.delete()
    return redirect('appointments')

def delete_notification(request, id):
    notification = Notification.objects.get(pk=id)
    notification.delete()
    return redirect('notifications')

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
        self_user = User1.objects.get(id_registarion = request.user.id)
        user_info = str(request.user)

        return render(request, 'main/profile.html', {'title': 'Профиль', 'self_user': self_user, 'user_info':user_info, 'appointments': appointments})
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

    return redirect('createacc')

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
        self_user = User1.objects.get(id_registarion=request.user.id)
        if request.method == "POST":
            self_user.name = request.POST.get("name")
            self_user.surname = request.POST.get("surname")
            self_user.save()
            return HttpResponseRedirect("/profile")
        else:
            return render(request, "main/edit-data.html", {'title': 'Редактирование профиля', "self_user": self_user})
    except self_user.DoesNotExist:
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

    return redirect('createacc')


def appointment_list(request):
    hospitals = Hospital.objects.all()
    return render(request, "main/index.html", {'title': 'Главная страница', 'hospitals': hospitals})