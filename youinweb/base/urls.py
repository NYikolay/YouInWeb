from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),

    path('', home, name='home'),
    path('profile/<str:pk>', userProfile, name='profile'),

    path('room/<int:pk>/', room, name='room'),
    path('create-room/', createRoom, name='create-room'),
    path('update-room/<str:pk>/', updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', deleteMessage, name='delete-message'),

    path('update-user/', updateUser, name='update-user'),
]
