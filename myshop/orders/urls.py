from django.urls import path
from myshop.orders import views


app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
]
