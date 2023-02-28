from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect


def products_view(request: WSGIRequest):
    return redirect('index')
