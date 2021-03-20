from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 製作物一覧
    path('products/', views.product_list, name='product_list'),
]
