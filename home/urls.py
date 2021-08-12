from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('resign_page/', views.resign_page, name='resign_page'),
    path('creat_patient/', views.crate_patient, name='crate_patient')
]