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
    path('daily-sales/', views.daily_sales, name='daily_sales'),  # Add this URL pattern
    path('record-expense/', views.record_expense, name='record_expense'),  # Add this URL pattern
    path('daily-summary/', views.daily_summary, name='daily_summary'),  # Add this URL pattern
    path('record-sale/', views.record_sale, name='record_sale'),
    path('sale-success/', views.sale_success, name='sale_success'),
    path('expenses-summary/', views.expenses_summary, name='expenses_summary'),
    path('send-daily-summary-email/', views.send_daily_summary_email, name='send_daily_summary_email'),

    # Add other URLs as needed
]



