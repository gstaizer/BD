from .models import User1, Notification, Hospital, Review, Doctor, Appointment
from django.forms import ModelForm, TextInput, Select, DateField


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ["id_user", "id_doctor", "time_to_appointment"]
        widgets = {
            "id_user": Select(attrs={
                'class': "form-control",
                'name': "id_user",
                'id': "id_user"
            }),
            "id_doctor": Select(attrs={
                'class': "form-control",
                'name': "id_doctor",
                'id': "id_doctor"
            }),
            "time_to_appointment": TextInput(attrs={

                'class': 'form-control',
                'type': 'datetime-local'
            })

        }

class UserForm(ModelForm):
    class Meta:
        model = User1
        fields = ["name", "surname", "avatar"]