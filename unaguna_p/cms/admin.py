from django.contrib import admin

from .models import Article, Product


# モデル Article の表示を定義
class ArticleAdmin(admin.ModelAdmin):
    # 一覧に表示するフィールド
    list_display = ('id', 'title', 'overview',)
    # 修正リンクでクリックできる項目
    list_display_links = ('id', 'title',)


# モデル Article を登録
admin.site.register(Article, ArticleAdmin)


# モデル Product を登録
admin.site.register(Product)
