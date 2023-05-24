from django import forms
from .models import *
from django.core.exceptions import ValidationError

class AddMessageForm(forms.ModelForm):
    #nickname = forms.CharField(max_length=50, label="Ник")
    #message = forms.CharField(widget=forms.Textarea(attrs={'cols':30, 'rows': 5}), label="Сообщение")
    class Meta:
        model = BoardMessages
        fields = ['nickname', 'message']
        widgets = {'nickname': forms.TextInput(attrs={'class': 'form-input'}),
                   'message': forms.Textarea(attrs={'cols':40, 'rows': 4}),
                   } # nickname -присвоение класса для дизайна, message- ширина, высота
    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        if len(nickname)>100:
            raise ValidationError('Длина привышает 100 символов')
        return nickname
