# Generated by Django 3.2 on 2022-01-27 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_appointmentcalander_updateuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentcalander',
            name='updatedt',
            field=models.DateTimeField(blank=True, db_column='UpdateDt', null=True),
        ),
        migrations.AlterField(
            model_name='appointmentcalander',
            name='updateuser',
            field=models.IntegerField(blank=True, db_column='UpdateUser', null=True),
        ),
    ]
