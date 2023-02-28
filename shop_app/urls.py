from django.urls import path

from shop_app.views.base import index_view


urlpatterns = [
    path("", index_view, name='index'),
    path('products', index_view, name='index'),
]
