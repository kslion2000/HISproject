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
def appointment(request):
    user_id = request.user.id
    user_info = New_user.objects.get(user_ptr_id=user_id)
    user_form = New_userForm(instance=user_info)
    site_key = settings.RECAPTCHA_SITE_KEY
    issue_old_data = AppointmentIssue.objects.filter(user_id_id=user_id)
    if request.method == 'POST':
        datas = dict(request.POST)
        datas['q_other'] = datas['q_other'][0]
        week_dic = {}

        #安全性驗證
        recaptcha_response = datas['g-recaptcha-response'][0]
        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if result['success'] != True:
            result = {'result': False, 'message': 'Security verification failed! Please try again.'}
            return HttpResponse(json.dumps(result), content_type='application/json')

        if issue_old_data:
            form = AppointmentIssueForm(datas, instance=issue_old_data[0])
            if form.is_valid():
                appointment_temp = form.save(commit=False)
                appointment_temp.user_id = user_info
                appointment_temp.updatedt = datetime.datetime.today()
                appointment_temp.save()
                result = {'result': True, 'message': 'Save success. We will arrange with it as soon as possible.'}
                return HttpResponse(json.dumps(result), content_type='application/json')

            else:
                errors = form.errors
                result = {'result': False, 'message': errors}
                return HttpResponse(json.dumps(result), content_type='application/json')
        else:
            form = AppointmentIssueForm(datas)
            if form.is_valid():
                appointment_temp = form.save(commit=False)
                appointment_temp.user_id = user_info
                appointment_temp.creatdt = datetime.datetime.today()
                appointment_temp.updatedt = datetime.datetime.today()
                appointment_temp.save()
                result = {'result': True, 'message': 'Save success. We will arrange with it as soon as possible.'}
                return HttpResponse(json.dumps(result), content_type='application/json')
            else:
                errors = form.errors
                return HttpResponse(json.dumps(errors), content_type='application/json')
    else:
        if issue_old_data:
            form = AppointmentIssueForm(instance=issue_old_data[0])
        else:
            form = AppointmentIssueForm()
        return render(request, 'users/appointment.html', locals())

def about(request):
    return render(request, 'users/about.html')