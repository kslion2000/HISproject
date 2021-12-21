from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('appointment/', views.appointment, name='appointment'),
    path('about/', views.about, name='about'),
]