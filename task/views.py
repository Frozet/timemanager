from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


data_db = [
    {'id': 1, 'title': 't1', 'content': 'text1', 'is_published': True},
    {'id': 2, 'title': 't2', 'content': 'text2', 'is_published': False},
    {'id': 3, 'title': 't3', 'content': 'text3', 'is_published': True},
]

# Create your views here.
def index(request):
    data = {
        'title': 'главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'timemanager/index.html', context=data)

def about(request):
    return render(request, 'timemanager/about.html', {'title': 'О сайте'})

def cats(request, cat_id):
    return HttpResponse(f'Страница с категориями<p>id: {cat_id}</p>')

def cats_path(request, cat_path):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'Страница с категориями<p>path: {cat_path}</p>')

def archive(request, year):
    if year > 2024:
        uri = reverse('cats', args=('alo', ))
        return HttpResponseRedirect(uri)
    return HttpResponse(f'Архив по годам<p>year: {year}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')