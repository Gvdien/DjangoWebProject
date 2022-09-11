from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# Create your views here.


rooms = [
    {"id":1,"name":"Page 1"},
    {"id":2,"name":"Page 2"},
    {"id":3,"name":"Page 3"}
]


def home(req):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(req, "home.html", context)

def room(req,key):
    room = Room.objects.get(id=key)
    context = {'room':room}
    return render(req, 'room.html',context)

def create_room(req):
    form = RoomForm()
    if req.method == "POST":
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form':form}
    return render(req, 'room_form.html',context)

def update_room(req,key):
    room = Room.objects.get(id=key)
    form = RoomForm(instance=room)
    if req.method == "POST":
        form = RoomForm(req.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form':form}
    return render(req, 'room_form.html',context)

def delete_room(req,key):
    room = Room.objects.get(id=key)
    if req.method == "POST":
        room.delete()
        return redirect('home')
    context ={'obj':room}
    return render(req, 'delete_room.html',context)