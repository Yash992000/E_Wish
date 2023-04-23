from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from auth_app.models import user, customer, merchant
from administrator.models import Categories,Sub_Categories,Diet
from merchant.models import product
from administrator.forms import SubCategoryForm,CategoryForm,DietForm
from django.core.paginator import Paginator
import csv
from reportlab.pdfgen import canvas

def admin(request):
    return render(request,'admin_index.html')
    
def admin_logout(request):
    return render(request,'admin_login.html')

def admin_mng_users(request):
    user1 = user.objects.all()
    p = Paginator(user1, 5)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)                   
    return render(request,'admin_mng_users.html', context={"userdata":page_obj}) # calls category page

def admin_mng_merchant(request):
    userProfile = user.objects.all()
    seller = merchant.objects.all()
    
    # merchUsers = user.objects.filter(user_type = 2)
    merchData = merchant.objects.filter(UserId__user_type = 2)
    
    p = Paginator(merchData, 5)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)                   
    return render(request,'admin_mng_merchant.html', context={"merchData":page_obj}) # calls category page

def admin_mng_customer(request):
    userProfile = user.objects.all()
    custom = customer.objects.all()
    
    # merchUsers = user.objects.filter(user_type = 2)
    custData = customer.objects.filter(UserId__user_type = 1)
    
    p = Paginator(custData, 5)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)                   
    return render(request,'admin_mng_customer.html', context={"custData":page_obj}) # calls category page

def deleteuser(request,id):
    context = {}
    obj = get_object_or_404(user,UserId=id)
    if obj.user_type == 1:
        cust = get_object_or_404(customer, UserId = id)
        if request.method == "GET":
            cust.delete()
    elif obj.user_type == 2:
        merch = get_object_or_404(merchant, UserId = id)  
        if request.method == "GET":
            merch.delete()
    
    if request.method == "GET":
        obj.delete()
        messages.success(request, "User deleted successfully!")
        return redirect("/admin_mng_users")
    else:
        messages.error(request, "Failed to delete user!")
        return render(request, "admin_mng_users.html", context)

def deleteseller(request,id):
    context = {}
    obj = get_object_or_404(merchant,MerchId=id)
    obj2 = get_object_or_404(user, UserId=obj.UserId.UserId)
    if request.method == "GET":
        obj2.user_type = 3
        obj2.save()
        obj.delete()
        messages.success(request, "Seller deleted successfully!")
        return redirect("/admin_mng_merchant")
    else:
        messages.error(request, "Failed to delete seller!")
        return render(request, "admin_mng_merchant.html", context)
    
def deletecustomer(request,id):
    context = {}
    obj = get_object_or_404(customer,CustomerId=id)
    obj2 = get_object_or_404(user, UserId=obj.UserId.UserId)
    if request.method == "GET":
        obj2.user_type = 3
        obj2.save()
        obj.delete()
        messages.success(request, "Customer deleted successfully!")
        return redirect("/admin_mng_customer")
    else:
        messages.error(request, "Failed to delete Customer!")
        return render(request, "admin_mng_customer.html", context)
    
