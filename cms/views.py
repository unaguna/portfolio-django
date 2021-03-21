from django.shortcuts import render

from .models import Product, Tag


def product_list(request):
    """記事の一覧
    """
    products = Product.objects.all().order_by('id')
    return render(request,
                  'cms/product_list.html',
                  {'products': products})


def product_list_by_tag(request, tag_id):
    """記事の一覧 (タグで絞込)
    """
    tag = Tag.objects.get(id=tag_id)
    articles = tag.article.all()
    print(articles)
    products = Product.objects.filter(article__in=articles).order_by('id')
    return render(request,
                  'cms/product_list.html',
                  {'products': products})
