# from django.contrib import auth_app
from django.urls import path
from .views import *

urlpatterns = [
    path('admin',admin,name='admin'),
    path('admin_categories',admin_categories,name='admin_categories'),
    path('admin_subcategories',admin_subcategories,name='admin_subcategories'),
    path('admin_dietary_preference',admin_dietary_preference,name='admin_dietary_preference'),
    path('admin_mng_products',admin_mng_products,name='admin_mng_products'),
    path('admin_feedback',admin_feedback,name='admin_feedback'),
    path('admin_mng_users',admin_mng_users,name='admin_mng_users'),
    path('admin_mng_merchant',admin_mng_merchant,name='admin_mng_merchant'),
    path('admin_mng_customer',admin_mng_customer,name='admin_mng_customer'),
    path('admin_logout',admin_logout,name='admin_logout'),

    path('toggle_product_approval/<id>', toggle_product_approval, name='toggle_product_approval'),

    path('deleteuser<id>',deleteuser,name='deleteuser'),
    path('deleteseller<id>',deleteseller,name='deleteseller'),
    path('deletecustomer<id>',deletecustomer,name='deletecustomer'),

    path('add_category',add_category,name='add_category'),
    path('deletecategory<id>',deletecategory,name='deletecategory'),
    path('admin_update_categories<id>',admin_update_categories,name='admin_update_categories'),
    path('editCategory/<id>',editCategory,name='editCategory'),

    path('add_subcategory',add_subcategory,name='add_subcategory'),
    path('deletesubcategory<id>',deletesubcategory,name='deletesubcategory'),
    path('admin_update_subcategories<id>',admin_update_subcategories,name='admin_update_subcategories'),
    path('editSubCategory/<id>',editSubCategory,name='editSubCategory'),

    path('add_dietary',add_dietary,name='add_dietary'),
    path('deletediet<id>',deletediet,name='deletediet'),
    path('admin_update_diet<id>',admin_update_diet,name='admin_update_diet'),
    path('editDiet/<id>',editDiet,name='editDiet'),
    

#downloads
    path('downloadCat',downloadCat,name="downloadCat"),
    path('downloadDiet',downloadDiet,name="downloadDiet"),
    path('downloadSubCat',downloadSubCat,name="downloadSubCat"),  
    path('downloadProduct',downloadProduct,name="downloadProduct"),  
    path('downloadUser',downloadUser,name="downloadUser"),
    
#uploads
    path('bulk_upload',bulk_upload,name="bulk_upload"),
    path('pie_chart',pie_chart,name="pie_chart"),
    path('city-report/', city_report, name='city-report'),


#recipe
    path('admin_recipe', admin_recipe, name="admin_recipe"),
    path('add_recipe', add_recipe, name="add_recipe"),
    path('admin_recipeIng', admin_recipeIng, name="admin_recipeIng"),
    path('add_recipeIng', add_recipeIng, name="add_recipeIng"),
    

]
