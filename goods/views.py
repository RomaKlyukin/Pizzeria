from unicodedata import category
from django.shortcuts import render

import goods
from goods.models import Products

def catalog(request, category_slug):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    products = Products.objects.all()

    context = {
        'title': 'Pizzeria - Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)
