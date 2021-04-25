from .models import User1, Notification, Hospital, Review, Doctor, Appointment, Avatar
from django.forms import ModelForm, TextInput, DateField
from django import forms


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ["id_user", "id_doctor", "time_to_appointment", "id_review"]

class UserForm(ModelForm):
    class Meta:
        model = User1
        fields = ["name", "surname", "avatar"]

class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ["avatar"]