from django.contrib import admin

# Register your models here.

from .models import *

class BoardMessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'message', 'time_created', 'isactive')
    list_display_links = ('id', 'nickname')
    search_fields = ('nickname', 'message')
    list_editable = ('isactive',)
    list_filter = ('time_created', 'isactive')

class MyPostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'posttext', 'postimage', 'time_created', 'isactive')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('isactive',)
    list_filter = ('time_created', 'isactive')

admin.site.register(BoardMessages, BoardMessagesAdmin)
admin.site.register(MyPosts, MyPostsAdmin)