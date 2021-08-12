from django import forms
from home.models import *
from django.core.exceptions import ValidationError
from string import ascii_letters
from django.core.validators import MaxLengthValidator

class PatientInformationForm(forms.Form):
    id = forms.CharField(required=True, widget=forms.TextInput, validators=[MaxLengthValidator(10, message='[ID] Ensure this value has at most 20 character.')])
    hosp = forms.CharField(required=True, widget=forms.TextInput, validators=[MaxLengthValidator(10, message='[ID] Ensure this value has at most 20 character.')])
    firstname = forms.CharField(required=True, widget=forms.TextInput, validators=[MaxLengthValidator(20, message='[ID] Ensure this value has at most 20 character.')])
    lastname = forms.CharField(required=True, widget=forms.TextInput, validators=[MaxLengthValidator(20, message='[ID] Ensure this value has at most 20 character.')])
    birthday = forms.DateField(required=False, widget=forms.DateInput)
    gender = forms.CharField(required=True, widget=forms.Select(choices=[('female', 'Female'),('male', 'Male')]))
    blood = forms.CharField(required=False, widget=forms.Select(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')]))
    tel = forms.CharField(required=False, widget=forms.TextInput, validators=[MaxLengthValidator(20, message='[ID] Ensure this value has at most 20 character.')])
    creatdt = forms.DateField(required=False, widget=forms.DateInput)

    class Mata:
        model = PatientInformation
        fields = ['id', 'hosp', 'firstname', 'lastname', 'birthday', 'gender', 'blood', 'tel', 'creatdt']
        exclude = ['Seq', 'modifydt']

    def id_format(self):
        id = self.cleaned_data['id']
        if id[0] not in ascii_letters or len(id) != 10 or id[1:11].isdigit() == False:
            raise ValidationError('%(value)s is not a correct ID number', params={'value': id})
        return id