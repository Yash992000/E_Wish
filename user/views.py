from django.shortcuts import render,redirect
from django.http import HttpResponse
from merchant.models import product

#from auth_app.forms import UserRegistrationForm  
#from auth_app.models import user_registration  

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

# def cart(request):
#     return render(request,'cart.html')

# def checkout(request):
#     return render(request,'checkout.html')

def contact_us(request):
    return render(request,'contact.html')

def gallery(request):
    obj = product.objects.all()
    return render(request,'gallery.html',{'image' : obj})

# def my_account(request):
#     return render(request,'my_account.html')

# def shop_detail(request):
#     return render(request,'shop_detail.html')

def shop(request):
    obj = product.objects.all()
    return render(request,'shop.html',{'product' : obj})

# def wishlist(request):
#     return render(request,'wishlist.html')

# def userlogout(request):
#     try:
#         del request.session['username'] 
#         del request.session['email'] 
#         del request.session['contact'] 
#         del request.session['shopName'] 
#         del request.session['shopAddr'] 
#         del request.session['shopPhone'] 
#         return render(request,'login.html')
#     except Exception as e:
#         return HttpResponse(e)
#     return render(request,'merchant_login.html')