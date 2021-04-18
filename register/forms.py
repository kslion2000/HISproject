from django import forms
from models import *
from django.core.exceptions import ValidationError
from string import ascii_letters

class PatientInformationForm(forms.Form):
    id = forms.CharField(required=True, attr=[])
    hosp = forms.CharField(required=True)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    birthday = forms.DateTimeField(required=False)
    gender = forms.CharField(required=True)
    blood = forms.CharField(required=False)
    tel = forms.CharField(required=False)
    creatdt = forms.DateTimeField(required=False)

    class Mata:
        model = PatientInformation
        fields = ['id', 'hosp', 'firstname', 'lastname', 'birthday', 'gender', 'blood', 'tel', 'creatdt']
        exclude = ['Seq', 'modifydt']

    def id_format(value):
        gender = '12'
        if value[0] not in ascii_letters or len(value) != 10 or value[1:11].isdigit() == False or value[1] not in gender:
            raise ValidationError('%(value)s is not an even number', params={'value': value})