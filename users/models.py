from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class New_user(User):
    contact_number = models.CharField(db_column='contact_number', max_length=20)

class AppointmentIssue(models.Model):
    seq = models.BigAutoField(db_column='Seq', primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    q_career = models.BooleanField(db_column='q_Career')
    q_family = models.BooleanField(db_column='q_Family')
    q_stress = models.BooleanField(db_column='q_Stress')
    q_relationship = models.BooleanField(db_column='q_Relationship')
    q_suicide = models.BooleanField(db_column='q_Suicide')
    q_violence = models.BooleanField(db_column='q_Violence')
    q_homo = models.BooleanField(db_column='q_Homo')
    q_trauma = models.BooleanField(db_column='q_Trauma')
    q_other = models.CharField(db_column='q_Other', max_length=300)
    creatdt = models.DateTimeField(db_column='CreatDt')
    updatedt = models.DateTimeField(db_column='UpdateDt')

class AppointmentWeek(models.Model):
    seq = models.BigAutoField(db_column='Seq', primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    weekday = models.CharField(db_column='WeekDay', max_length=15)
    morning = models.BooleanField(db_column='Morning')
    afternoon = models.BooleanField(db_column='Afternoon')
    evening = models.BooleanField(db_column='Evening')

