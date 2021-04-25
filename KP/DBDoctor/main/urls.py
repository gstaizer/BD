from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create-appointment', views.createappointment, name='create-appointment'),
    path('appointment-list', views.appointment_list, name='appointment-list'),
    path('id_up_status/', views.id_up_status, name='id_up_status'),
    path('id_down_status/', views.id_down_status, name='id_down_status'),
    path('profile', views.profile, name='profile'),
    path('create-account', views.createacc, name='createacc'),
    path('edit-data', views.edit_data, name='edit-data'),
    path('edit-avatar/', views.edit_avatar,  name='edit-avatar'),
    path('appointments', views.appointments,  name='appointments'),
    path('notifications', views.notifications,  name='notifications'),
    path('delete-notification/<id>', views.delete_notification,  name='delete-notification'),
    path('doctors', views.doctors,  name='doctors'),
    path('delete-appointment/<id>', views.delete_appointment, name='delete-appointment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)