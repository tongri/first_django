from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .forms import EnglishForm, LoginForm, LogoutForm, SearchForm, RegistrationForm
from django.views.generic import FormView
from django.contrib.auth import login, authenticate, logout
import random
import string

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from app.models import Article, Comment


class EnglishFormView(FormView):
    http_method_names = ['post', 'get']
    form_class = EnglishForm
    success_url = '/thanks/'

    def get(self, request, *args, **kwargs):
        form = EnglishForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = EnglishForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            level = form.cleaned_data['level']
            gender = form.cleaned_data['pol']
            if gender == 'm' and level in ['B2', 'C1', 'C2'] and age > 20:
                return HttpResponseRedirect('/thanks/')
            elif gender == 'f' and level in ['B1', 'B2', 'C1', 'C2'] and age > 22:
                return HttpResponseRedirect('/thanks/')
            else:
                return HttpResponseRedirect('/sorry/')


class LoginFormView(FormView):
    http_method_names = ['get', 'post']
    form_class = LoginForm
    success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        form = request.POST
        username = form['name']
        password = form['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/articles/')
        else:
            return HttpResponseRedirect('/sorry/')

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})


class LogoutFormView(LoginRequiredMixin, FormView):
    http_method_names = ['get', 'post']
    form_class = LogoutForm
    login_url = "/login/"

    def get(self, request, *args, **kwargs):
        form = LogoutForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/articles/')


class SearchFormView(FormView):
    http_method_names = ['get', 'post']
    form_class = SearchForm

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        return render(request, 'comments.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            look = form.cleaned_data['field']
            matches = Comment.objects.filter(msg__icontains=look)
            return render(request, 'comments.html', {'form':form, 'matches': matches})

class RegistrationFormView(FormView):
    http_method_names = ['get', 'post']
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request)


def nologin(request):
    return HttpResponse('wrong password or username')


def thanks(request):
    return HttpResponse('Thanks for your info')


def sorry(request):
    return HttpResponse('Sorry, but you dont meet our demands')


def first(request):
    return render(request, 'static.html', {
        'name': 'test',
    })


def index(request):
    slugger = ''.join(random.choices(string.ascii_lowercase, k=5))
    article_id = random.randint(0, 99999)
    return render(request, 'static.html', {
        'slugger': slugger,
        'article_id': article_id,
        'name': 'main',
    })


def articles(request):
    arts = Article.objects.all()
    return render(request, 'static.html', {
        'name': 'users',
        'arts': arts,
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


def phone(request, phone):
    return render(request, 'phone.html', {
        'phone': phone,
    })


def uniq(request, unique):
    return render(request, 'slugger.html', {
        'unique': unique,
    })
