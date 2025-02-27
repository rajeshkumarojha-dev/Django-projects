from django.forms import ModelForm
from .models import Todo

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.validators import MinLengthValidator

class TodoForm(ModelForm):
    class Meta:
        model=Todo
        fields=['todo']
        labels={'todo':''}


class SignInForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','email']

class LogInForm(AuthenticationForm):
    class Meta:
        model= User
        fields=['username','password']