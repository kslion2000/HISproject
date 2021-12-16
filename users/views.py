from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import HttpResponse
from django.contrib import messages
from .forms import *
from users.models import New_user
from django.conf import settings
import requests
import json
import datetime

def register(request):
    if request.method == 'POST':
        form = New_userForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = New_userForm()
    return render(request, 'users/register.html', {'form': form})

@login_required()
def appointment(request, monday={}, tuesday={}, wednesday={}, thursday={}, friday={}, saturday={}, sunday={}):
    user_id = request.user.id
    user_info = New_user.objects.get(user_ptr_id=user_id)
    user_form = New_userForm(instance=user_info)
    site_key = settings.RECAPTCHA_SITE_KEY
    issue_old_data = AppointmentIssue.objects.filter(user_id_id=user_id)
    week_old_data = AppointmentWeek.objects.filter(user_id_id=user_id)
    if request.method == 'POST':
        datas = dict(request.POST)
        save_data = []
        for key in datas.keys():
            if key.startswith('mon'):
                monday[key.split('_')[1]] = True
            if key.startswith('tue'):
                tuesday[key.split('_')[1]] = True
            if key.startswith('wed'):
                wednesday[key.split('_')[1]] = True
            if key.startswith('thu'):
                thursday[key.split('_')[1]] = True
            if key.startswith('fri'):
                friday[key.split('_')[1]] = True
            if key.startswith('sat'):
                saturday[key.split('_')[1]] = True
            if key.startswith('sun'):
                sunday[key.split('_')[1]] = True
        print(monday)
        datas['q_other'] = datas['q_other'][0]
        if issue_old_data:
            form = AppointmentIssueForm(datas, instance=issue_old_data[0])
            if form.is_valid():
                appointment_temp = form.save(commit=False)
                appointment_temp.user_id = user_info
                appointment_temp.updatedt = datetime.datetime.today()
                appointment_temp.save()
            else:
                errors = form.errors
                print(errors)
        else:
            form = AppointmentIssueForm(datas)
            if form.is_valid():
                appointment_temp = form.save(commit=False)
                appointment_temp.user_id = user_info
                appointment_temp.creatdt = datetime.datetime.today()
                appointment_temp.updatedt = datetime.datetime.today()
                appointment_temp.save()
            else:
                errors = form.errors
                print(errors)

        print(aaa)
        recaptcha_response = datas.getlist('g-recaptcha-response')[0]
        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result['success']:
            result = {'result': True, 'message': 'Save success.'}
            return HttpResponse(json.dumps(result), content_type='application/json')
        else:
            result = {'result': False, 'message': 'Fail!'}
            return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        if issue_old_data:
            form = AppointmentIssueForm(instance=issue_old_data[0])
        else:
            form = AppointmentIssueForm()
        return render(request, 'users/appointment.html', locals())