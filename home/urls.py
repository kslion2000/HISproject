from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('spuser_managepage/', views.spuser_managepage, name='spuser_managepage'),
    path('update_news/', views.update_news, name='update_news'),
    path('load_news/', views.load_news, name='load_news'),

]