# from django.contrib import auth_app
from django.urls import path
from . import views

urlpatterns = [
    path('merchant',views.merchant,name='merchant'),
    path('merchant_add_products',views.merchant_add_products,name='merchant_add_products'),
    path('merchant_logout',views.merchant_logout,name='merchant_logout'),
]