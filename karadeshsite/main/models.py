from django.db import models

# Create your models here.

class BoardMessages(models.Model):
    nickname = models.CharField(max_length=100, verbose_name='Ник')
    message = models.TextField(blank=True, verbose_name='Сообщение')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    isactive = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "Сообщения на стене"
        verbose_name_plural = "Сообщения на стене"
        ordering = ['-time_created','nickname']

class MyPosts(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    posttext = models.TextField(blank=True, verbose_name='Текст')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    postimage = models.ImageField(upload_to="images/", verbose_name='Изображение')
    isactive = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Мои посты"
        verbose_name_plural = "Мои посты"
        ordering = ['-time_created','title']