from django.db import models
from datetime import date, datetime

class User1(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    id_registarion = models.IntegerField()
    avatar = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Notification(models.Model):
    id_user = models.ForeignKey(User1, on_delete=models.CASCADE)
    notification_text = models.CharField('Текст уведомления', max_length=50)

    def __str__(self):
        return self.notification_text

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'



class Hospital(models.Model):
    name_h = models.CharField('Наименование', max_length=100)
    address = models.CharField('Адрес', max_length=50)
    telephone = models.CharField('Телефон', max_length=50)

    def __str__(self):
        return self.name_h

    class Meta:
        verbose_name = 'Госпиталь'
        verbose_name_plural = 'Госпитали'


class Review(models.Model):
    comment = models.CharField('Комментарий', max_length=50)
    appraisal = models.IntegerField('Оценка')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Doctor(models.Model):
    full_name = models.CharField('ФИО', max_length=50)
    speciality = models.CharField('Специальность', max_length=50)
    id_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

class Avatar(models.Model):
    title = models.CharField('Имя', max_length=10)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

class Appointment(models.Model):
    time_to_appointment = models.DateField(("Дата"), default=date.today)
    nower = datetime.now()
    name_app = "Регистрация посещения: " + nower.strftime('%d/%m/%Y')
    id_user = models.ForeignKey(User1, on_delete=models.CASCADE)
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    id_review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_app

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'