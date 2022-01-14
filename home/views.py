from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from djangoProject.commonfunction import *
import requests
from home.models import *
import home
from home.forms import *
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
