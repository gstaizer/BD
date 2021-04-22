from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create-appointment', views.create, name='create'),
    path('appointment-list', views.appointment_list, name='appointment-list'),
]