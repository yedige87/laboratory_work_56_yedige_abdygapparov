from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from shop_app.models import Product, CategoryChoice


def index_view(request: WSGIRequest):
    products = Product.objects.exclude(price=0)
    context = {
        'products': products, 'choices': CategoryChoice.choices
    }
    return render(request, 'index.html', context=context)
