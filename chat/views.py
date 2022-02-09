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
    if request.method == "POST":
        if not Room.objects.filter(name=request.POST['room_name']).first():
            Room.objects.create(
                name=request.POST['room_name'], password=request.POST['password'])
            return redirect(reverse('room', kwargs={'room_name': request.POST['room_name']}))
        else:
            room = Room.objects.get(name=request.POST.get('room_name'))
            if request.POST['password'] == room.password:
                return redirect(reverse('room', kwargs={'room_name': request.POST['room_name']}))
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})


@login_required
def room(request, room_name):
    username = request.user.username
    messages = Message.objects.filter(room=room_name)[0:25]
    profanity.load_censor_words()
    return render(
        request, 'chat/room.html',
        {'room_name': room_name,
         'username': username,
         'messages': messages
         })


class Signup(View):
    def get(self, request):
        form = forms.RegisterForm()
        return render(request, "chat/signup.html", {'form': form})

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username'])
            login(self.request, user)
            return redirect(reverse('index'))
        else:
            return render(self.request, 'chat/signup.html', {'form': form})
