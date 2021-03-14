from django.http import HttpResponse


def article_list(request):
    """記事の一覧
    """
    return HttpResponse('書籍の一覧')
