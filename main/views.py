from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Pizzeria - Главная',
        'content': 'Доставка пиццы PIZZERIA',
    }
    return render(request, 'main\index.html', context)

def about(request):
    context = {
        'title': 'Pizzeria - О нас',
        'content': 'О нас',
        'text_on_page': 'Pizzeria - это сеть пиццерий с большим разнообразным ассортиментом и быстрой доставкой.',
    }
    return render(request, 'main/about.html', context)
    
