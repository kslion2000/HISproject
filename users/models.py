from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class New_user(User):
    contact_number = models.CharField(db_column='contact_number', max_length=20)

class AppointmentIssue(models.Model):
    seq = models.BigAutoField(db_column='Seq', primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    q_career = models.BooleanField(db_column='q_Career', blank=True)
    q_family = models.BooleanField(db_column='q_Family', blank=True)
    q_stress = models.BooleanField(db_column='q_Stress', blank=True)
    q_relationship = models.BooleanField(db_column='q_Relationship', blank=True)
    q_suicide = models.BooleanField(db_column='q_Suicide', blank=True)
    q_violence = models.BooleanField(db_column='q_Violence', blank=True)
    q_homo = models.BooleanField(db_column='q_Homo', blank=True)
    q_trauma = models.BooleanField(db_column='q_Trauma', blank=True)
    q_other = models.CharField(db_column='q_Other', max_length=300, blank=True)
    creatdt = models.DateTimeField(db_column='CreatDt', blank=True)
    updatedt = models.DateTimeField(db_column='UpdateDt', blank=True)

class AppointmentWeek(models.Model):
    seq = models.BigAutoField(db_column='Seq', primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    mon_m = models.BooleanField(db_column='mon_m')
    mon_a = models.BooleanField(db_column='mon_a')
    mon_e = models.BooleanField(db_column='mon_e')
    tue_m = models.BooleanField(db_column='tue_m')
    tue_a = models.BooleanField(db_column='tue_a')
    tue_e = models.BooleanField(db_column='tue_e')
    wed_m = models.BooleanField(db_column='wed_m')
    wed_a = models.BooleanField(db_column='wed_a')
    wed_e = models.BooleanField(db_column='wed_e')
    thu_m = models.BooleanField(db_column='thu_m')
    thu_a = models.BooleanField(db_column='thu_a')
    thu_e = models.BooleanField(db_column='thu_e')
    fri_m = models.BooleanField(db_column='fri_m')
    fri_a = models.BooleanField(db_column='fri_a')
    fri_e = models.BooleanField(db_column='fri_e')
    sat_m = models.BooleanField(db_column='sat_m')
    sat_a = models.BooleanField(db_column='sat_a')
    sat_e = models.BooleanField(db_column='sat_e')
    sun_m = models.BooleanField(db_column='sun_m')
    sun_a = models.BooleanField(db_column='sun_a')
    sun_e = models.BooleanField(db_column='sun_e')

