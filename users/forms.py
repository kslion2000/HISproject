from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import *
from django.core.validators import MaxLengthValidator

class New_userForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta:
        model = New_user
        fields = ['first_name', 'last_name', 'username', 'email', 'contact_number', 'password1', 'password2']

class AppointmentIssueForm(forms.ModelForm):
    mon_m = forms.BooleanField(required=False)
    mon_a = forms.BooleanField(required=False)
    mon_e = forms.BooleanField(required=False)
    tue_m = forms.BooleanField(required=False)
    tue_a = forms.BooleanField(required=False)
    tue_e = forms.BooleanField(required=False)
    wed_m = forms.BooleanField(required=False)
    wed_a = forms.BooleanField(required=False)
    wed_e = forms.BooleanField(required=False)
    thu_m = forms.BooleanField(required=False)
    thu_a = forms.BooleanField(required=False)
    thu_e = forms.BooleanField(required=False)
    fri_m = forms.BooleanField(required=False)
    fri_a = forms.BooleanField(required=False)
    fri_e = forms.BooleanField(required=False)
    sat_m = forms.BooleanField(required=False)
    sat_a = forms.BooleanField(required=False)
    sat_e = forms.BooleanField(required=False)
    sun_m = forms.BooleanField(required=False)
    sun_a = forms.BooleanField(required=False)
    sun_e = forms.BooleanField(required=False)
    q_career = forms.BooleanField(required=False)
    q_family = forms.BooleanField(required=False)
    q_stress = forms.BooleanField(required=False)
    q_relationship = forms.BooleanField(required=False)
    q_suicide = forms.BooleanField(required=False)
    q_violence = forms.BooleanField(required=False)
    q_homo = forms.BooleanField(required=False)
    q_trauma = forms.BooleanField(required=False)
    q_other = forms.CharField(required=False, validators=[
        MaxLengthValidator(300, message='[Other problem] Ensure this value in has at most 300 character.')])

    class Meta:
        model = AppointmentIssue
        exclude = ['user_id', 'creatdt', 'updatedt']

class AppointmentCalanderForm(forms.ModelForm):
    note = forms.CharField(required=False, validators=[
        MaxLengthValidator(100, message='[Note] Ensure this value in has at most 100 character.')])

    class Meta:
        model = AppointmentCalander
        exclude = ['seq', 'creatuser', 'creatdt', 'updatedt']