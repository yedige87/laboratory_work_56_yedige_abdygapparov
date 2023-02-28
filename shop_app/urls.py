from django.urls import path

from shop_app.views.base import index_view
from shop_app.views.products import product_view, product_delete_view, confirm_delete

urlpatterns = [
    path("", index_view, name='index'),
    path('products', index_view, name='index'),
    path('products/<int:pk>', product_view, name='product_view'),
    path('product/<int:pk>/delete', product_delete_view, name='product_delete'),
    path('product/delete/<int:pk>', confirm_delete, name='confirm_delete'),
]
