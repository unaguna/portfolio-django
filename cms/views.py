from django.http import Http404
from django.shortcuts import render

from .models import Product, Tag, Article


def product_page(request, article_id):
    """記事（製作物）
    """
    try:
        article = Article.objects.get(id=article_id)
        product = Product.objects.get(article=article)
    except Exception:
        raise Http404("The article doesn't exist.")

    # 記事本文が公開されていないページは表示しない
    if article.body is None or article.body == '':
        raise Http404("The article has no body.")

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
