from django.db import models


class Article(models.Model):
    """記事
    """
    title = models.CharField('タイトル', max_length=255)
    overview = models.TextField('概要')
    body = models.TextField('本文', blank=True)
    url_github = models.CharField('GitHub URL', max_length=255, blank=True)
    url_chrome_store = models.CharField('GoogleChrome URL', max_length=255, blank=True)

    def __str__(self):
        return self.title
