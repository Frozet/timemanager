from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string

from task.models import Task

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


data_db = [
    {'id': 1, 'title': 't1', 'content': 'text1', 'is_published': True},
    {'id': 2, 'title': 't2', 'content': 'text2', 'is_published': False},
    {'id': 3, 'title': 't3', 'content': 'text3', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'cat1'},
    {'id': 2, 'name': 'cat2'},
    {'id': 3, 'name': 'cat3'},
]

# Create your views here.
def index(request):
    posts = Task.published.all()
    data = {
        'title': 'главная страница',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'timemanager/index.html', context=data)

def about(request):
    return render(request, 'timemanager/about.html', {'title': 'О сайте', 'menu': menu})

def show_post(request, post_slug):
    post = get_object_or_404(Task, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'timemanager/post.html', data)

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_category(request, cat_id):
    return index(request)

def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')