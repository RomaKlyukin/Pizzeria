from unicodedata import category
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

import goods
from goods.models import Products

def catalog(request, category_slug, page=1):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 2)
    current_page = paginator.page(page)

    context = {
        'title': 'Pizzeria - Каталог',
        'goods': current_page,
        "slug_url": category_slug
    }
    return render(request, 'goods/catalog.html', context)
