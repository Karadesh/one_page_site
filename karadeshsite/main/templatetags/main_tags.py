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