from django.db import models

# Create your models here.
class PatientInformation(models.Model):
    gender = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    Seq = models.BigAutoField(db_column='Seq', primary_key=True)
    id = models.CharField(db_column='ID', blank=False)
    hosp = models.CharField(db_column='Hosp', blank=False)
    firstname = models.CharField(db_column='FirstName', blank=False)
    lastname = models.CharField(db_column='LastName', blank=False)
    birthday = models.DateTimeField(db_column='LastName', blank=False)
    gender = models.CharField(db_column='Gender', choices=gender, blank=True, null=True)
    blood = models.CharField(db_column='Blood', max_length=3, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=20, blank=True, null=True)
    creatdt = models.DateTimeField(db_column='CreatDt', auto_now_add=True)
    modifydt = models.DateTimeField(db_column='ModifyDt', auto_now=True)

    class Meta:
        db_table = "register"