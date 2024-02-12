from django import template
import task.views as views
from task.models import Category

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories():
    return views.cats_db


@register.inclusion_tag('timemanager/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
