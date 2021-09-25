from django.contrib import admin
from django.urls import path
from account.views import *



urlpatterns = [
    path('signin/', signin, name="signin"),
    path('signup/', signup, name="signup"),
]