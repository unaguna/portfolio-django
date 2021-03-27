from django.shortcuts import render

from .models import Product, Tag, Article


def product_page(request, article_id):
    """記事（製作物）
    """
    article = Article.objects.get(id=article_id)
    product = Product.objects.get(article=article)
    return render(request,
                  'cms/product.html',
                  {'product': product})


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
    products = Product.objects.filter(article__in=articles).order_by('id')
    return render(request,
                  'cms/product_list.html',
                  {'products': products})
