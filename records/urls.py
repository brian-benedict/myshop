from django.urls import path
from . import views

urlpatterns = [
    path('add/product/', views.add_product, name='add_product'),
    path('add/category/', views.add_category, name='add_category'),
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
]
