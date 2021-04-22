from django.contrib import admin
from .models import User, Notification, Hospital, Review, Doctor, Appointment

admin.site.register(User)
admin.site.register(Notification)
admin.site.register(Hospital)
admin.site.register(Review)
admin.site.register(Doctor)
admin.site.register(Appointment)