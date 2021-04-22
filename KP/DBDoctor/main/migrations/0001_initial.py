# Generated by Django 3.2 on 2021-04-14 07:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_h', models.CharField(max_length=50, verbose_name='Наименование')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
                ('telephone', models.CharField(max_length=50, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=50, verbose_name='Комментарий')),
                ('appraisal', models.IntegerField(max_length=1, verbose_name='Оценка')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('login', models.CharField(max_length=50, verbose_name='Логин')),
                ('email', models.CharField(max_length=50, verbose_name='Эл Почта')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_text', models.CharField(max_length=50, verbose_name='Текст уведомления')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('speciality', models.CharField(max_length=50, verbose_name='Специальность')),
                ('id_hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hospital')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_to_appointment', models.DateField(default=datetime.date.today, verbose_name='Дата')),
                ('id_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctor')),
                ('id_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.review')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
            options={
                'verbose_name': 'Посещение',
                'verbose_name_plural': 'Посещения',
            },
        ),
    ]
