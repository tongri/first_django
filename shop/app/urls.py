from django.contrib import admin
from django.urls import path, include, re_path

from app.views import first, archive, articles, article_number, article_number_archive, users, phone, uniq

urlpatterns = [
    path('test/', first),
    path('articles/', articles, name='mail-article'),
    path('articles/archive/', archive, name='archive'),
    path('users/', users, name='users'),
    path('article/<int:article_id>/', article_number, name='article-with-number'),
    path('article/<int:article_id>/archive/', article_number_archive, name='archive-with-num'),
    path('article/<int:article_id>/<slug:slug_text>/', article_number, name='slug-article'),
    path('users/<int:user_num>/', users, name='users-with-num'),
    re_path(r'(?P<phone>0(?:98|97|66|67|68)\d{7})/', phone, name='for-correct_phones'),
    re_path(r'(?P<unique>\A([a-f0-9]){4}-([a-f0-9]{6}))\b', uniq, name='unique'),
]