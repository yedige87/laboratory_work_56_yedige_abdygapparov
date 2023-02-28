from django.urls import path

from shop_app.views.base import index_view
from shop_app.views.products import product_view


urlpatterns = [
    path("", index_view, name='index'),
    path('products', index_view, name='index'),
    path('products/<int:pk>', product_view, name='product_view'),

]
