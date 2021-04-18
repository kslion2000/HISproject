from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    response = requests.get(
        "https://emma.pixnet.cc/mainpage/blog/categories/hot/28") #28為國內旅遊
    articles = response.json()["articles"] #轉換為JSON物件後，存取articles欄位
    return render(request, "posts/index.html", {"articles": articles})

def resign_page(request):
    return render(request, 'basic/resign_page.html')

def crate_patient(request):
    return render(request, 'basic/crate_patient.html')
