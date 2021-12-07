from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class New_user(User):
    contact_number = models.CharField(db_column='contact_number', max_length=20)