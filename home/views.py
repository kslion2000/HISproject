from django.shortcuts import render
import requests
import home
from home.forms import *


# Create your views here.
def index(request):
    response = requests.get(
        "https://emma.pixnet.cc/mainpage/blog/categories/hot/33")
    articles = response.json()["articles"] #轉換為JSON物件後，存取articles欄位
    return render(request, "home/home.html", {"articles": articles})
