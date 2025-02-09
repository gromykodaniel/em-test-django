from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('order/new/', views.creat_order, name='order_create'),
    path('order/<int:pk>/edit/', views.update_order, name='order_update'),
    path('order/<int:pk>/delete/', views.order_delete, name='order_delete'),
    path('revenue/', views.total_revenue, name='total_revenue'),
]
