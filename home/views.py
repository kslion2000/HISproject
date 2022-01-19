from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from djangoProject.commonfunction import *
import requests
from home.models import *
import home
from home.forms import *
from users.models import *
from users.forms import *
from datetime import datetime
import json
from os import listdir


# Create your views here.
def index(request):
    response = requests.get(
        "https://emma.pixnet.cc/mainpage/blog/categories/hot/33")
    articles = response.json()["articles"] #轉換為JSON物件後，存取articles欄位
    all_news = LatestNews.objects.filter(active=1).order_by('-creatdt')
    return render(request, "home/home.html", locals())

@is_superuser
def spuser_managepage(request):
    return render(request, "home/spuser_managepage.html")

@is_superuser
def update_news(request):
    if request.method == 'POST':
        data = request.POST
        form = LatestNewsForm(data)
        # 判斷是否為舊資料
        if data.get("seq"):
            record = LatestNews.objects.filter(seq=data.get("seq"))
            form = LatestNewsForm(data, instance=record[0])
            if form.is_valid():
                submit_form = form.save(commit=False)
                submit_form.active = int(data.get('active'))
                submit_form.updatedt = datetime.today()
                submit_form.save()
                result = {'result': True, 'message': 'Save success.'}
            else:
                message = error_dict_convert(form.errors)
                result = {'result': False, 'message': message}
        else:
            form = LatestNewsForm(data)
            if form.is_valid():
                submit_form = form.save(commit=False)
                submit_form.active = int(data.get('active'))
                submit_form.user_id_id = request.user.id
                submit_form.creatdt = datetime.today()
                submit_form.updatedt = datetime.today()
                submit_form.save()
                result = {'result': True, 'message': 'Save success.'}
            else:
                message = error_dict_convert(form.errors)
                result = {'result': False, 'message': message}
        return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        len = int(request.GET.get('getData', 0))
        if len:
            new_data = LatestNews.objects.filter().order_by('-creatdt')[len-1:len+9].values(
                'seq', 'news_title', 'news_content', 'news_location', 'creatdt', 'news_link', 'active')
            for data in new_data:
                data['creatdt'] = data['creatdt'].strftime("%b. %d/%Y, %H:%M:%S")
            return HttpResponse(json.dumps(list(new_data)), content_type='application/json')

        img_files = listdir("static/img")
        original_news = LatestNews.objects.filter().order_by('-creatdt')[:15]
        return render(request, "home/update_news.html", locals())

@is_superuser
def load_news(request):
    if request.method == 'GET':
        seq = request.GET.get('seq')
        select_news = LatestNews.objects.filter(seq=seq).values(
            'seq', 'news_title', 'news_content', 'news_link', 'active', 'news_location')
    return HttpResponse(json.dumps(list(select_news)), content_type='application/json')

@is_superuser
def load_app(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        app_data = AppointmentIssue.objects.filter(user_id_id=id).values(
            'mon_m', 'mon_a', 'mon_e', 'tue_m', 'tue_a', 'tue_e', 'wed_m', 'wed_a', 'wed_e', 'thu_m', 'thu_a', 'thu_e',
            'fri_m', 'fri_a', 'fri_e', 'sat_m', 'sat_a', 'sat_e', 'sun_m', 'sun_a', 'sun_e', 'q_career', 'q_family',
            'q_stress', 'q_relationship', 'q_suicide', 'q_violence', 'q_homo', 'q_trauma', 'q_other')
    return HttpResponse(json.dumps(list(app_data)), content_type='application/json')

@is_superuser
def schedule_arrangement(request):
    app_list = New_user.objects.filter(is_active=True).order_by('-app_active', 'last_login')
    return render(request, "home/schedule_arrangement.html", locals())

@is_superuser
def update_app_active(request):
    id = request.GET.get('id')
    status = True if request.GET.get('status') == 'true' else False
    New_user.objects.filter(user_ptr_id=id).update(app_active=status)
    result = {'message': 'Update success'}
    return HttpResponse(json.dumps(result), content_type='application/json')
