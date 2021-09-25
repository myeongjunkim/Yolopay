from django.contrib import admin
from django.urls import path
from mainpage.views import *



urlpatterns = [
    path('', main, name="main"),
    path('calendar/', calendar, name="calendar"),
]