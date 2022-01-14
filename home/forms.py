from django import forms
from home.models import *
from django.core.exceptions import ValidationError
from string import ascii_letters
from django.core.validators import MaxLengthValidator

class LatestNewsForm(forms.ModelForm):
    seq = forms.IntegerField(required=False)
    news_title = forms.CharField(required=True, label='Title', validators=[MaxLengthValidator(100, message='Ensure [Title] has at most 100 character.')])
    news_content = forms.CharField(required=True, label='Content', validators=[MaxLengthValidator(400, message='Ensure [Content] has at most 400 character.')])
    news_link = forms.CharField(required=True, label='Link', validators=[MaxLengthValidator(200, message='Ensure [Link] has at most 400 character.')])
    news_location = forms.CharField(required=True, label='Icon')
    active = forms.BooleanField(required=True, label='Active')

    class Meta:
        model = LatestNews
        fields = ['seq', 'news_title', 'news_content', 'news_link', 'news_location', 'active']

    def __init__(self, *args, **kwargs):
        super(LatestNewsForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': 'The field [{fieldname}] is required.'.format(
                fieldname=field.label)}