from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound, Http404
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

#return redirect('adress') for redirect 302 
# and ('adress', permanent=True) for redirect 301 

#raise Http404(for raise 404 error)

# Create your views here.

class Homepage(ListView):
    model = MyPosts
    template_name = 'main/index.html'
    context_object_name = 'posts' #имя словаря модели MyPosts в шаблоне
    #extra_context = {'title': 'Главная'} передавать стат. данные: строку (словари, списки нельзя)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context
    
    def get_queryset(self):
        return MyPosts.objects.filter(isactive=True)
    #Добавить в контекст страницы разные приколямбы через шаманские фокусы

class ShowPost(DetailView):
    model = MyPosts
    template_name = 'main/show_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context
#def show_post(request, post_slug):
#    post = get_object_or_404(MyPosts, slug=post_slug)
#    context = {
#        'title': post.title,
#        'post': post
#    }
#    return render(request, "main/show_post.html", context=context)

def feedback(request):
    context = {
        'title': 'feedback'
    }
    return render(request, "main/feedback.html", context=context)

def about(request):
    context = {
        'title': 'about'
    }
    return render(request, "main/about.html", context=context)

class Boardpage(CreateView):
    form_class = AddMessageForm
    #model = BoardMessages
    template_name = 'main/board.html'
    success_url = reverse_lazy('board')
    #context_object_name = 'posts' #имя словаря модели MyPosts в шаблоне
    #extra_context = {'title': 'Главная'} передавать стат. данные: строку (словари, списки нельзя)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Board'
        return context
    
    #def get_queryset(self):
    #    return MyPosts.object.filter(isactive=True)

#def board(request): #Добавить page_num, чтобы можно было смотреть страницы
#    if request.method == 'POST':
#        form = AddMessageForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('board')
#    1else:
#        form = AddMessageForm()
#    context = {
#        'title': 'Board',
#        'form': form
#    }
#    return render(request, "main/board.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("Page not found")