from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound, Http404
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
    context = {
        'menu': menu,
        'title': 'Karadesh site'
    }
    return render(request, "main/index.html", context=context)

def show_post(request, post_slug):
    post = get_object_or_404(MyPosts, slug=post_slug)
    context = {
        'menu': menu,
        'title': post.title,
        'post': post
    }
    return render(request, "main/show_post.html", context=context)

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
    context = {
        'menu': menu,
        'title': 'Board',
    }
    return render(request, "main/board.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("Page not found")