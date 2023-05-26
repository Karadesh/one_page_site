from django.urls import path
from .views import *

urlpatterns = [
    path('', Homepage.as_view(), name='home'), #names for redirect on them
    path('feedback/', feedback, name='feedback'),
    path('about/', about, name='about'),
    path('board/', Boardpage.as_view(), name='board'), #добавить <int:page_num> для страниц с пагинацией
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
]