# Generated by Django 3.2 on 2021-04-14 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='appraisal',
            field=models.IntegerField(verbose_name='Оценка'),
        ),
    ]
