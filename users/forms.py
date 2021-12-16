from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import *
from django.core.validators import MaxLengthValidator

class New_userForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    contact_number = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta:
        model = New_user
        fields = ['first_name', 'last_name', 'username', 'email', 'contact_number', 'password1', 'password2']

class AppointmentWeekForm(forms.ModelForm):
    weekday = forms.CharField()
    morning = forms.BooleanField()
    afternoon = forms.BooleanField()
    evening = forms.BooleanField()

    class Meta:
        model = AppointmentWeek
        fields = ['weekday', 'morning', 'afternoon', 'evening']

class AppointmentIssueForm(forms.ModelForm):
    q_career = forms.BooleanField(required=False)
    q_family = forms.BooleanField(required=False)
    q_stress = forms.BooleanField(required=False)
    q_relationship = forms.BooleanField(required=False)
    q_suicide = forms.BooleanField(required=False)
    q_violence = forms.BooleanField(required=False)
    q_homo = forms.BooleanField(required=False)
    q_trauma = forms.BooleanField(required=False)
    q_other = forms.CharField(max_length=300, required=False)

    class Meta:
        model = AppointmentIssue
        exclude = ['user_id', 'creatdt', 'updatedt']