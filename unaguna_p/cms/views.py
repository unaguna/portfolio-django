from django.shortcuts import render

from .models import Article


def article_list(request):
    """記事の一覧
    """
    articles = Article.objects.all().order_by('id')
    return render(request,
                  'cms/article_list.html',
                  {'articles': articles})
