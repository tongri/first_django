from django.contrib import admin

# Register your models here.
from app.models import Article, Person, Mark, Comment

admin.site.register(Article)
admin.site.register(Person)
admin.site.register(Comment)
admin.site.register(Mark)
