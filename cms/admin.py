from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Article, Product


class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article


# モデル Article の表示を定義
class ArticleAdmin(ImportExportModelAdmin):
    # 一覧に表示するフィールド
    list_display = ('id', 'title', 'overview',)
    # 修正リンクでクリックできる項目
    list_display_links = ('id', 'title',)

    # django-import-exportsの設定
    resource_class = ArticleResource


# モデル Article を登録
admin.site.register(Article, ArticleAdmin)


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


# モデル Article の表示を定義
class ProductAdmin(ImportExportModelAdmin):
    # django-import-exportsの設定
    resource_class = ProductResource


# モデル Product を登録
admin.site.register(Product, ProductAdmin)
