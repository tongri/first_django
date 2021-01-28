from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse

from .forms import EnglishForm, LoginForm, LogoutForm, SearchForm, RegistrationForm, CommentForm, ChangePassword
from django.views.generic import FormView
from django.contrib.auth import login, authenticate, logout
import random
import string
from django.contrib.auth.models import User


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
        return render(request, 'registr.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username, email=None, password=password)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponse('great')
        else:
            return HttpResponse('passwords didnt match')

class ChangePasswordView(LoginRequiredMixin, FormView):
    http_method_names = ['get', 'post']
    form_class = ChangePassword

    def get(self, request, *args, **kwargs):
        form = ChangePassword()
        user = request.user
        return render(request, 'form.html', {'form': form, 'user': user})

    def post(self, request, *args, **kwargs):
        form = ChangePassword(request.POST)
        if form.is_valid():
            old = form.cleaned_data.get('old')
            u = authenticate(request, username=request.user, password=old)
            if u is not None:
                changed = User.objects.get(username=u.username)
                changed.set_password(form.cleaned_data.get('new_conf'))
                changed.save()
            else:
                return HttpResponse('sorry - old password is wrong')
            return HttpResponse('nice')
        else:
            return HttpResponse("Passwords do not match")



class CommentFormView(FormView):
    http_method_names = ['get', 'post']
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        form = CommentForm()
        arts = Article.objects.all()
        comms = Comment.objects.all()
        return render(request, 'static.html', {'arts': arts, 'form': form, 'comms': comms})

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            msg = form.cleaned_data.get('msg')
            art_id = form.data.get('art_id')
            user = request.user
            place = Article.objects.filter(id=art_id)[0]
            Comment.objects.create(user=user, msg=msg, place=place)
        return HttpResponseRedirect(reverse('mail-article'))


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

def comment(request, article_id):
    return HttpResponse(f'{article_id}')
