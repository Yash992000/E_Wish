from django.shortcuts import render,redirect
#from django.http import HttpResponse
#from auth_app.forms import UserRegistrationForm  
#from auth_app.models import user_registration  

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def contact_us(request):
    return render(request,'contact_us.html')

def gallery(request):
    return render(request,'gallery.html')

def my_account(request):
    return render(request,'my_account.html')

def shop_detail(request):
    return render(request,'shop_detail.html')

def shop(request):
    return render(request,'shop.html')

def wishlist(request):
    return render(request,'wishlist.html')
