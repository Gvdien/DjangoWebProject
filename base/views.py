from django.shortcuts import render

# Create your views here.


rooms = [
    {"id":1,"Name":"Page 1"},
    {"id":2,"Name":"Page 2"},
    {"id":3,"Name":"Page 3"}
]


def home(req):
    context = {"rooms": rooms}
    return render(req, "home.html", context)

def room(req,key):
    room = None
    for i in rooms:
        if i['id'] == int(key):
            room = i
    context = {'room':room}
    return render(req, 'room.html',context)