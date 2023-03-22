# from django.contrib import auth_app
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('registration',views.registration,name='registration'),
    path('merchant_login',views.merchant_login,name='merchant_login'),
    path('merchant_registration',views.merchant_registration,name='merchant_registration'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin',views.admin,name='admin'),
    path('register',views.register,name='register'),
    path('log',views.log,name='log'),

    path('seller_register',views.seller_register,name='seller_register'),
    path('seller_log',views.seller_log,name='seller_log'),

    path('admin_log',views.admin_log,name='admin_log'),

]