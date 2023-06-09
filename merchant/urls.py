# from django.contrib import auth_app
from django.urls import path
from . import views

urlpatterns = [
    path('merchant_index',views.merchant_index,name='merchant_index'),
    path('merchant_add_products',views.merchant_add_products,name='merchant_add_products'),
    path('merchant_update_product<id>',views.merchant_update_product,name='merchant_update_product'),
    path('merchant_manage_product',views.merchant_manage_product,name='merchant_manage_product'),
    path('deleteproduct<id>',views.deleteproduct,name='deleteproduct'),
    path('merchant_profile',views.merchant_profile,name='merchant_profile'),
    path('merchant_profile_update',views.merchant_profile_update,name='merchant_profile_update'),
    path('merchant_profile_edit/<id>',views.merchant_profile_edit,name='merchant_profile_edit'),
    path('merchant_change_pswd',views.merchant_change_pswd,name='merchant_change_pswd'),
    path('change_password',views.change_password,name='change_password'),
    path('merchant_logout',views.merchant_logout,name='merchant_logout'),

    path('addProduct',views.addProduct,name='addProduct'),
    path('editproduct/<id>',views.editproduct,name='editproduct'),

]