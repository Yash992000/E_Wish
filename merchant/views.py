from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
# from Login.forms import SignUpForm  
# from Login.models import SignUp  

# Create your views here.
def merchant(request):
    return render(request,'merchant_index.html')

def merchant_add_products(request):
    return render(request,'merchant_add_products.html')

def merchant_logout(request):
    return render(request,'merchant_login.html')