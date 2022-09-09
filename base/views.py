from django.shortcuts import render
from .models import Room
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