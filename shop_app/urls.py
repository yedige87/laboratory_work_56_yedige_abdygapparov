from django.urls import path

from shop_app.views.base import index_view
from shop_app.views.products import product_view, product_delete_view, confirm_delete, product_add_view, \
    product_edit_view, category_view

urlpatterns = [
    path("", index_view, name='index'),
    path('products', index_view, name='index'),
    path('products/<int:pk>', product_view, name='product_view'),
    path('product/<int:pk>/delete', product_delete_view, name='product_delete'),
    path('product/delete/<int:pk>', confirm_delete, name='confirm_delete'),
    path('products/add', product_add_view, name='product_add'),
    path('product/<int:pk>/edit', product_edit_view, name='product_edit'),
    path('products/<str:cat_id>', category_view, name='category_view'),

]
