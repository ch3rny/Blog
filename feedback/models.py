from django.db import models
from django.utils import timezone


# Create your models here.
class Review(models.Model):
    author = models.CharField(max_length=75, blank=False, verbose_name='Ваше имя')
    mail = models.EmailField(verbose_name='Ваш e-mail', default='', blank=True)
    theme = models.CharField(max_length=200, verbose_name='Тема', default='', blank=True)
    text = models.TextField(verbose_name='Содержимое')
    created_time = models.DateTimeField(default=timezone.now)
    attachment = models.FileField(upload_to='reviews', default=None, blank=True, verbose_name='Вложение')
    unread = models.BooleanField(default=True)

