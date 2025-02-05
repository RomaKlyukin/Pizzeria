from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Pizzeria - Главная',
        'content': 'Доставка пиццы PIZZERIA',
        "categories": categories
    }
    return render(request, 'main\index.html', context)

def about(request):
    context = {
        'title': 'Pizzeria - О нас',
        'content': 'О нас',
        'text_on_page': 'Pizzeria - это сеть пиццерий с большим разнообразным ассортиментом и быстрой доставкой.',
    }
    return render(request, 'main/about.html', context)
    
