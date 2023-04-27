from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('profile',views.profile,name='profile'),
    # path('cart',views.cart,name='cart'),
    # path('checkout',views.checkout,name='checkout'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('gallery',views.gallery,name='gallery'),
    # path('my_account',views.my_account,name='my_account'),
    # path('shop_detail',views.shop_detail,name='shop_detail'),
    path('shop',views.shop,name='shop'),
    # path('wishlist',views.wishlist,name='wishlist'),
    path('userlogout',views.userlogout,name='userlogout'),
    
    path('add_to_cart/<id>',views.add_to_cart,name="add_to_cart"),
    path('cart', views.cart, name = 'cart'),

    path('changePassword',views.changePassword,name='changePassword'),
    path('user_change_password',views.user_change_password,name='user_change_password'),
    
    # path('checkout', views.checkout, name = 'checkout'),
    # path('updatecart', views.updateCart, name = 'updatecart'),
    # path('updatequantity', views.updateQuantity, name = 'updatequantity'),
]