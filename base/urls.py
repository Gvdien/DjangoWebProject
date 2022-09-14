from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name ="home"),
    path('room/<str:key>/',views.room,name ="room"),
    path('create-room/',views.create_room,name ="create-room"),
    path('update-room/<str:key>/',views.update_room,name ="update-room"),
    path('delete-room/<str:key>/',views.delete_room,name ="delete-room"),
    path('login/',views.loginUser,name ="login"),
    path('logout/',views.logoutUser,name ="logout"),
    path('register/',views.registerUser,name ="register"),
]