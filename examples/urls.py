from django.urls import path, re_path
from . import views

# app_name = AppName

urlpatterns = [
    path('', views.person, name='personpage')
]

