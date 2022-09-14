from django.shortcuts import render, redirect
from .models import Room, Topic, User
from .forms import RoomForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.


def loginUser(req):
    page = 'login'
    if req.user.is_authenticated:
        return redirect('home')

    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(req, 'User does not exist')

        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            messages.error(req, 'Username or password is not correct')
            return redirect('login')
    context = {'page': page}
    return render(req, 'login_register.html', context)

def logoutUser(req):
    logout(req)
    return redirect('login')


def registerUser(req):
    form = UserCreationForm()

    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(req, 'Account was created for ' + user)
            return redirect('login')
        else:
            messages.error(req, 'An error has occured during registration')
            return redirect('register')

    return render(req, 'login_register.html', {'form': form})

def home(req):
    q = req.GET.get('q') if req.GET.get('q') is not None else ""
    rooms = Room.objects.filter(topic__name__icontains=q)
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {"rooms": rooms, "topics": topics, 'room_count': room_count}
    return render(req, "home.html", context)


def room(req, key):
    room = Room.objects.get(id=key)
    room_messages = room.message_set.all()
    context = {'room': room, 'room_messages': room_messages}
    return render(req, 'room.html', context)

@login_required(login_url='loginUser')
def create_room(req):
    form = RoomForm()
    if req.method == "POST":
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(req, 'room_form.html', context)

@login_required(login_url='login')
def update_room(req, key):
    room = Room.objects.get(id=key)
    form = RoomForm(instance=room)

    if req.user != room.host:
        return HttpResponse("You are not allowed to do this")

    if req.method == "POST":
        form = RoomForm(req.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(req, 'room_form.html', context)

@login_required(login_url='login')
def delete_room(req, key):
    room = Room.objects.get(id=key)
    if req.method == "POST":
        room.delete()
        return redirect('home')
    context = {'obj': room}
    return render(req, 'delete_room.html', context)
