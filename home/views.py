from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, is_superuser
import requests
from home.models import *
import home
from home.forms import *
from datetime import datetime
import json


# Create your views here.
def index(request):
    response = requests.get(
        "https://emma.pixnet.cc/mainpage/blog/categories/hot/33")
    articles = response.json()["articles"] #轉換為JSON物件後，存取articles欄位
    return render(request, "home/home.html", {"articles": articles})

@is_superuser
def spuser_managepage(request):
    # request = requests.get(f"http://{request.META.get('HTTP_HOST', '')}/home")
    # if request.status_code == 200:
    #     print('Web site exists')
    # else:
    #     print('Web site does not exist')
    return render(request, "home/spuser_managepage.html")

@is_superuser
def update_news(request):
    original_news = LatestNews.objects.filter().order_by('-creatdt')
    return render(request, "home/update_news.html", locals())

def load_news(request):
    if request.method == 'GET':
        seq = request.GET.get('seq')
        select_news = LatestNews.objects.filter(seq=seq).values(
            'seq', 'news_title', 'news_content', 'news_link', 'active')

    return HttpResponse(json.dumps(list(select_news)), content_type='application/json')
