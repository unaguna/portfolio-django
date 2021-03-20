from django.shortcuts import render

from .models import Product


def product_list(request):
    """記事の一覧
    """
    products = Product.objects.all().order_by('id')
    return render(request,
                  'cms/product_list.html',
                  {'products': products})
