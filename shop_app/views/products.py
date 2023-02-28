import os

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, get_object_or_404, render

from shop_app.forms import ProductForm
from shop_app.models import CategoryChoice, Product


def products_view(request: WSGIRequest):
    return redirect('index')


def product_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', context={'choices': CategoryChoice.choices, 'product': product})


def product_delete_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'delete.html', context=context)


def confirm_delete(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')


def product_add_view(request: WSGIRequest):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'product_add.html', context={'choices': CategoryChoice.choices, 'form': form})
    # POST
    form = ProductForm(data=request.POST)
    print(form.__dict__)
    if not form.is_valid():
        return render(request, 'product_add.html', context={'choices': CategoryChoice.choices, 'form': form})
    else:
        prod_data = {
            'title': request.POST.get('title'),
            'price': request.POST.get('price'),
            'photo': request.POST.get('photo'),
            'description': request.POST.get('description'),
            'category': request.POST.get('category'),
            'qty': request.POST.get('qty'),
        }
        if not os.path.exists('/static/images/' + prod_data['photo']):
            prod_data['photo'] = 'blank.jpg'

        Product.objects.create(**prod_data)
        return redirect('index')


def product_edit_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(instance=product)
        return render(request, 'product_edit.html',
                      context={'choices': CategoryChoice.choices, 'form': form, 'product': product})

    form = ProductForm(data=request.POST)
    print(form.__dict__)
    if not form.is_valid():
        return render(request, 'product_edit.html',
                      context={'choices': CategoryChoice.choices, 'form': form, 'product': product})
    else:
        product.title = request.POST.get('title')
        product.price = request.POST.get('price')
        product.photo = request.POST.get('photo')
        product.description = request.POST.get('description')
        product.category = request.POST.get('category')
        product.qty = request.POST.get('qty')

        if not os.path.exists('/static/images/' + product.photo):
            product.photo = 'blank.jpg'

        product.save()
        return redirect('index')


def category_view(request: WSGIRequest, cat_id):
    products = Product.objects.filter(category=cat_id)
    context = {
        'products': products, 'choices': CategoryChoice.choices, 'category_name': cat_id
    }
    return render(request, 'category_view.html', context=context)