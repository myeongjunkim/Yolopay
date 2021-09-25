from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import UserProfile


class SignupForm(forms.Form):
    class Meta:
        model = User

    name = forms.CharField(max_length=30)
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "placeholder": ("E-mail address"),
                "autocomplete": "email",
            }
        )
    )
    age = forms.IntegerField()
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': "form-control"}))

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2
    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_name = User.objects.filter(username=username)
        if user_name.exists:
            raise forms.ValidationError("Username already exists. Please try again.")
        return username
        
    def signup(self, request, user):
        userProfile = UserProfile()
        userProfile.user = user
        userProfile.name = self.cleaned_data[('name')]
        userProfile.email = user.email
        userProfile.age = self.cleaned_data[('age')]
        userProfile.save()
        user.save()
        return user