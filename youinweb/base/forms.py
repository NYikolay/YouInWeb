from django.forms import ModelForm
from .models import *


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class MessagesForm(ModelForm):
    class Meta:
        model = Message
        fields = ('body', )
