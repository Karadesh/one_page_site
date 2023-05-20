from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

#return redirect('adress') for redirect 302 
# and ('adress', permanent=True) for redirect 301 

#raise Http404(for raise 404 error)

# Create your views here.
menu = [{"title": "Board", "url_name": "board"},
        {"title": "Обо мне", "url_name": "about"}, 
        {"title":"Мои проекты", "url_name": "about"},
        {"title":"Задонатить", "url_name":"https://www.donationalerts.com/r/karadesh"}]

def index(request):
    my_posts = MyPosts.objects.all()
    context = {
        'my_posts': my_posts,
        'menu': menu,
        'title': 'Karadesh site'
    }
    return render(request, "main/index.html", context=context)

def feedback(request):
    context = {
        'menu': menu,
        'title': 'feedback'
    }
    return render(request, "main/feedback.html", context=context)

def about(request):
    context = {
        'menu': menu,
        'title': 'about'
    }
    return render(request, "main/about.html", context=context)

def board(request): #Добавить page_num, чтобы можно было смотреть страницы
    posts = BoardMessages.objects.all()
    context = {
        'menu': menu,
        'title': 'Board',
        'posts': posts
    }
    return render(request, "main/board.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("Page not found")