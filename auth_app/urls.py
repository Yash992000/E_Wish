# from django.contrib import auth_app
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('Cregistration',views.Cregistration,name='Cregistration'),
    path('merchant_login',views.merchant_login,name='merchant_login'),
    path('merchant_registration',views.merchant_registration,name='merchant_registration'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin',views.admin,name='admin'),
    path('register',views.register,name='register'),
    path('log',views.log,name='log'),
]