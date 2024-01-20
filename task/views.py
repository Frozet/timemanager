from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    # t = render_to_string('timemanager/index.html')
    # return HttpResponse(t)
    return render(request, 'timemanager/index.html')

def about(request):
    return render(request, 'timemanager/about.html')

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