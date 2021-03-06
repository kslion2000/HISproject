# Generated by Django 3.2 on 2022-01-27 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_user',
            name='app_active',
            field=models.BooleanField(db_column='app_active', default=False),
        ),
        migrations.CreateModel(
            name='AppointmentCalander',
            fields=[
                ('seq', models.BigAutoField(db_column='Seq', primary_key=True, serialize=False)),
                ('start', models.CharField(blank=True, db_column='start', max_length=20)),
                ('end', models.CharField(blank=True, db_column='end', max_length=20)),
                ('note', models.CharField(blank=True, db_column='note', max_length=100)),
                ('creatuser', models.IntegerField(blank=True, db_column='CreatUser')),
                ('creatdt', models.DateTimeField(blank=True, db_column='CreatDt')),
                ('updatedt', models.DateTimeField(blank=True, db_column='UpdateDt')),
                ('app_user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
