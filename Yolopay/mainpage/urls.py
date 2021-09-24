from django.contrib import admin
from django.urls import path
from mainpage.views import *



urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('calendar/', calendar, name="calendar"),
    path('create/', create, name="create")
    
]