# from django.contrib import auth_app
from django.urls import path
from . import views

urlpatterns = [
    path('admin',views.admin,name='admin'),
    path('admin_categories',views.admin_categories,name='admin_categories'),
    path('admin_subcategories',views.admin_subcategories,name='admin_subcategories'),
    path('admin_dietary_preference',views.admin_dietary_preference,name='admin_dietary_preference'),
    path('admin_mng_products',views.admin_mng_products,name='admin_mng_products'),
    path('admin_feedback',views.admin_feedback,name='admin_feedback'),
    path('admin_mng_users',views.admin_mng_users,name='admin_mng_users'),
    path('admin_mng_merchant',views.admin_mng_merchant,name='admin_mng_merchant'),
    path('admin_mng_customer',views.admin_mng_customer,name='admin_mng_customer'),
    path('admin_logout',views.admin_logout,name='admin_logout'),

    path('toggle_product_approval/<id>', views.toggle_product_approval, name='toggle_product_approval'),

    path('deleteuser<id>',views.deleteuser,name='deleteuser'),
    path('deleteseller<id>',views.deleteseller,name='deleteseller'),
    path('deletecustomer<id>',views.deletecustomer,name='deletecustomer'),

    path('add_category',views.add_category,name='add_category'),
    path('deletecategory<id>',views.deletecategory,name='deletecategory'),
    path('admin_update_categories<id>',views.admin_update_categories,name='admin_update_categories'),
    path('editCategory/<id>',views.editCategory,name='editCategory'),

    path('add_subcategory',views.add_subcategory,name='add_subcategory'),
    path('deletesubcategory<id>',views.deletesubcategory,name='deletesubcategory'),
    path('admin_update_subcategories<id>',views.admin_update_subcategories,name='admin_update_subcategories'),
    path('editSubCategory/<id>',views.editSubCategory,name='editSubCategory'),

    path('add_dietary',views.add_dietary,name='add_dietary'),
    path('deletediet<id>',views.deletediet,name='deletediet'),
    path('admin_update_diet<id>',views.admin_update_diet,name='admin_update_diet'),
    path('editDiet/<id>',views.editDiet,name='editDiet'),

#downloads
    path('downloadCat',views.downloadCat,name="downloadCat"),
    path('downloadDiet',views.downloadDiet,name="downloadDiet"),
    path('downloadSubCat',views.downloadSubCat,name="downloadSubCat"),  
]