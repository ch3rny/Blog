from platform import mac_ver

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField


class Category(models.Model):
    category = models.CharField(max_length=200)
    numbirs = models.IntegerField()

    def __str__(self):
        return self.category


class Post(models.Model):
    author = models.ForeignKey('auth.User', verbose_name="Автор")
    title = models.CharField(max_length=200, verbose_name="Название")
    text = RichTextField(blank=True, default='', verbose_name="Содержимое")
    cover = models.ImageField(upload_to='articles', default='/article.png', verbose_name="Иллюстрация")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    category = models.ForeignKey('Category', verbose_name="Рубрика")
    likes = models.ManyToManyField('UserProfile', verbose_name='Лукасы')
    watched = models.IntegerField(default=0, verbose_name='Просмотры')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    profile_image = ImageField(upload_to='avatars',default='avatar.png', verbose_name="Аватар")


    def __str__(self):
        return self.user.first_name+' '+self.user.last_name


class Comment(models.Model):
    author = models.ForeignKey('auth.User', verbose_name="Автор")
    author_avatar = models.ForeignKey('UserProfile')
    sourse = models.CharField(max_length=200)
    text = models.TextField(verbose_name="Оставьте ваш комментарий:")
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания")

    def __str__(self):
        return str(self.created_date)+' '+self.text
