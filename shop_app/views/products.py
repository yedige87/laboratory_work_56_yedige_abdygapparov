from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, get_object_or_404, render

from shop_app.models import CategoryChoice, Product


def products_view(request: WSGIRequest):
    return redirect('index')


def product_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={'choices': CategoryChoice.choices, 'product': product})