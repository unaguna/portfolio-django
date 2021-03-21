from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 製作物一覧
    path('products/', views.product_list, name='product_list'),
    path('products/tag/<int:tag_id>', views.product_list_by_tag, name='product_list'),
]
