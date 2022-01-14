from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LatestNews(models.Model):
    seq = models.BigAutoField(db_column='Seq', primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    news_title = models.CharField(db_column='NewsTitle', max_length=100, blank=True)
    news_content = models.CharField(db_column='NewsContent', max_length=400, blank=True)
    news_link = models.CharField(db_column='NewsLink', max_length=200, blank=True)
    news_location = models.CharField(db_column='NewsLocation', max_length=50, blank=True)
    active = models.BooleanField(db_column='Active', blank=True)
    creatdt = models.DateTimeField(db_column='CreatDt', blank=True)
    updatedt = models.DateTimeField(db_column='UpdateDt', blank=True)
