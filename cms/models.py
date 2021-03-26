from django.db import models


class Tag(models.Model):
    """タグ
    """
    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField('タグ名', max_length=255)
    priority_rank = models.IntegerField('優先順位', default=255, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('priority_rank',)


class Article(models.Model):
    """記事
    """
    title = models.CharField('タイトル', max_length=255)
    overview = models.TextField('概要')
    body = models.TextField('本文', blank=True)
    tag_list = models.ManyToManyField(Tag, related_name='article')

    def __str__(self):
        return self.title

    def get_tag_list(self):
        return self.tag_list.order_by('priority_rank')


class Product(models.Model):
    """製作物
    """
    article = models.OneToOneField(Article, verbose_name='記事', related_name='product', on_delete=models.CASCADE)
    url_product = models.CharField('Product URL', max_length=255, blank=True)
    url_document = models.CharField('Document URL', max_length=255, blank=True)
    url_github = models.CharField('GitHub URL', max_length=255, blank=True)
    url_android = models.CharField('Google Play URL', max_length=255, blank=True)
    url_pypi = models.CharField('PyPI', max_length=255, blank=True)
    url_chrome_store = models.CharField('GoogleChrome URL', max_length=255, blank=True)
    url_firefox_addons = models.CharField('Firefox ADD-ONS URL', max_length=255, blank=True)

    def __str__(self):
        return self.article.title
