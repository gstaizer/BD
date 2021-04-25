from .models import User1, Notification, Hospital, Review, Doctor, Appointment, Avatar
from django.forms import ModelForm, TextInput, Select, DateField


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ["id_user", "id_doctor", "time_to_appointment"]

class UserForm(ModelForm):
    class Meta:
        model = User1
        fields = ["name", "surname", "avatar"]

class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ["avatar"]