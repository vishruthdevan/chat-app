from django import forms
from django.forms import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=50)

    class Meta(UserCreationForm.Meta):
        model = User
