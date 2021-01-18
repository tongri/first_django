from django.shortcuts import render
import random
import string

# Create your views here.

from django.http import HttpResponse

def first(request):
    return render(request, 'static.html', {
        'name': 'test',
    })

class MyClass:
    string = ''
    def __init__(self, s):
        self.string = s


def index(request):
    slugger = ''.join(random.choices(string.ascii_lowercase, k = 5))
    article_id = random.randint(0, 99999)
    return render(request, 'static.html', {
        'slugger': slugger,
        'article_id': article_id,
        'name': 'main',
    })

def articles(request):
    return render(request, 'static.html', {
        'name': 'users',
    })

def archive(request):
    return render(request, 'static.html', {
        'name': 'archive page',
    })

def users(request, user_num=0):
    return render(request, 'static.html', {
        'name': 'users',
    })

def article_number(request, article_id, slug_text=''):
    return render(request, "dynamic.html", {
        'article_id': article_id,
        'slug_text': slug_text,
    })

def article_number_archive(request, article_id):
    return render(request, 'articles.html', {
        'article_id': article_id,
    })

def articles(request):
    return render(request, 'articles.html')

def phone(request, phone):
    return render(request, 'phone.html', {
        'phone': phone,
    })

def uniq(request, unique):
    return render(request, 'slugger.html', {
        'unique': unique,
    })
