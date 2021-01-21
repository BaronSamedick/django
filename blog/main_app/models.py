from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class User(User):
    pass


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    body = models.TextField('Содержание')
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    created = models.DateTimeField('Дата публикации', default=datetime.now)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
