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
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)