from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cats/<int:cat_id>', views.cats, name='cats_id'),
    path('cats/<path:cat_path>', views.cats_path, name='cats'),
    path('archive/<year4:year>/', views.archive, name='archive')
]
