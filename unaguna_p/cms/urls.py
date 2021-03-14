from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 書籍
    path('', views.article_list, name='article_list'),
]
