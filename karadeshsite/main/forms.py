from django import forms
from .models import *

class AddMessageForm(forms.Form):
    nickname = forms.CharField(max_length=50, label="Ник")
    message = forms.CharField(widget=forms.Textarea(attrs={'cols':30, 'rows': 5}), label="Сообщение")
