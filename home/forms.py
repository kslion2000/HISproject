from django import forms
from home.models import *
from django.core.exceptions import ValidationError
from string import ascii_letters
from django.core.validators import MaxLengthValidator

