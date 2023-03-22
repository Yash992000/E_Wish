from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('gallery',views.gallery,name='gallery'),
    path('my_account',views.my_account,name='my_account'),
    path('shop_detail',views.shop_detail,name='shop_detail'),
    path('shop',views.shop,name='shop'),
    path('wishlist',views.wishlist,name='wishlist'),
    
]