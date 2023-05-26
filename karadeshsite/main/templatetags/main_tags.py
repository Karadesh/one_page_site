from django import template
from main.models import *

register = template.Library()

@register.simple_tag() #name= for use category with chosen name
def get_posts(filter=None):
    if not filter:
        return MyPosts.objects.all()
    else:
        return MyPosts.objects.filter(pk=filter)

@register.simple_tag()
def get_board(filter=None):
    if not filter:
        return BoardMessages.objects.all()
    else:
        return BoardMessages.objects.filter(pk=filter)
    
@register.inclusion_tag('main/menu.html')
def show_menu():
    menu = [{"title": "Board", "url_name": "board"},
        {"title": "Обо мне", "url_name": "about"}, 
        {"title":"Мои проекты", "url_name": "about"},
        {"title":"Задонатить", "url_name":"https://www.donationalerts.com/r/karadesh"}]
    return {"menu": menu}