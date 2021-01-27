from datetime import datetime, timedelta

from django.utils import timezone
from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'People'


class Article(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField(default=None)
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='articles', default=None)
    choice = models.ManyToManyField(Person, related_name='positive', blank=True, through='Mark', default=None)

    def __str__(self):
        return self.name

class Mark(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    opts = (('l', 'like'), ('d', 'dislike'))
    mark = models.CharField(max_length=10, choices=opts, default=None)

    def __str__(self):
        return '{}: {} to {}'.format(self.person.name, 'like' if self.mark == 'l' else 'dislike', self.article.name)


class Comment(models.Model):
    place = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(Person, default=None, blank=True, on_delete=models.CASCADE)
    msg = models.TextField(max_length=100, default=None)
    to_message = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, default=None)
    created_at = models.DateField(auto_now=True, null=True)
    updated_at = models.DateField(auto_now_add=True, null=True)

    def save(self, **kwargs):
        super().save()
        if not self.id:
            self.created_at = timezone.now() - timedelta(days=365)

    def __str__(self):
        return f'{self.user}: {self.msg[:10]}'
