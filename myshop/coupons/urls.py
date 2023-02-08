from django.urls import path

from myshop.coupons import views


app_name = 'coupons'

urlpatterns = [
    path('apply/', views.coupon_apply, name='apply'),
]
