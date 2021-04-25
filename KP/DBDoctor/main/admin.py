from django.contrib import admin
from .models import User1, Notification, Hospital, Review, Doctor, Appointment

admin.site.register(User1)
admin.site.register(Notification)
admin.site.register(Hospital)
admin.site.register(Review)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.site_header = 'Управление сайтом "Doctor+"'