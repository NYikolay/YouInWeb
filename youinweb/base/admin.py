from django.contrib import admin
from .models import *


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'topic', 'updated', 'created')
    list_display_links = ('name', )
    search_fields = ('name', 'host', 'updated', 'created')
    list_editable = ('topic', )
    list_filter = ('host', 'updated', 'created')
    list_per_page = 10


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'updated', 'created')
    list_display_links = ('user', 'room')
    search_fields = ('user', 'room', 'created')
    list_filter = ('user', 'room', 'created')
    list_per_page = 10


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')

