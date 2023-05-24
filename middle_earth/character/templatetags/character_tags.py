from django import template
from character.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('character/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag('character/menu.html')
def show_menu():
    menu = [{'title': "About website", 'url_name': 'about'},
        {'title': "Create new page", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'feedback'}
            ]
    menu2 = [
        {'title': "Register", 'url_name': 'register'},
        {'title': "Login", 'url_name': 'login'}
            ]

    return {"menu": menu}