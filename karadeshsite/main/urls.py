from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'), #names for redirect on them
    path('feedback/', feedback, name='feedback'),
    path('about/', about, name='about'),
    path('board/', board, name='board'), #добавить <int:page_num> для страниц с пагинацией
]