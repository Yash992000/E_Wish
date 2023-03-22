# from django.contrib import auth_app
from django.urls import path
from . import views

urlpatterns = [
    path('admin',views.admin,name='admin'),
    path('admin_categories',views.admin_categories,name='admin_categories'),
    path('admin_subcategories',views.admin_subcategories,name='admin_subcategories'),
    path('admin_mng_products',views.admin_mng_products,name='admin_mng_products'),
    path('admin_feedback',views.admin_feedback,name='admin_feedback'),
    path('admin_mng_users',views.admin_mng_users,name='admin_mng_users'),
    path('admin_mng_merchant',views.admin_mng_merchant,name='admin_mng_merchant'),

    path('deleteuser<id>',views.deleteuser,name='deleteuser'),
    path('deleteseller<id>',views.deleteseller,name='deleteseller'),

]