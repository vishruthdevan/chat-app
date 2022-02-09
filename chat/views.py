from django.forms import PasswordInput
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import login
# Create your views here.
from .models import Message, Room
from better_profanity import profanity


def index(request):

    return render(request, 'chat/index.html')
