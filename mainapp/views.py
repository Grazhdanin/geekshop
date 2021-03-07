from django.shortcuts import render
from mainapp.models import Product, ProductCategory
import os

dir = os.path.dirname(__file__)

def index(request):
    context = {'title': 'GeekShop',
               'name': 'GeekShop Store'}
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):
    context = {
        'tittle': "GeekShop",
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),

    }
    return render(request, 'mainapp/products.html', context)