from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from auth_app.models import user,merchant
from administrator.models import Categories,Sub_Categories,Diet
from merchant.forms import ProductForm
from merchant.models import product

from auth_app.forms import merchantReg
from django.contrib.auth.hashers import make_password , check_password


# # Create your views here.
def merchant_index(request):
    return render(request,'merchant_index.html')

def merchant_add_products(request):
    context = { 'product_data' : product.objects.all().select_related('categoryName','subcategoryName','dietType').order_by('productId'),'category':Categories.objects.all().order_by('categoryId'),'subcategory':Sub_Categories.objects.all().order_by('subcategoryId'),'diet':Diet.objects.all().order_by('dietId')}
    return render(request,'merchant_add_products.html',{'context': context})

def merchant_manage_product(request):
    # product_data = {}
    obj = product.objects.all()
    return render(request,'merchant_manage_product.html', {'product_data' : obj})

def addProduct(request):  
    if request.method == "POST": 
        c_form = ProductForm(request.POST or None, request.FILES) 
        # return HttpResponse(c_form)
        if c_form.is_valid():
            c_form.save()
            messages.success(request, "Product inserted successfully!")
            context = { 'subcategory_data': product.objects.all()}
            return render(request,'merchant_add_products.html',{'context': context})
        
        else:
            messages.error(request, "Product insertion failed!")
            return render(request,'merchant_add_products.html')
    else:
        messages.error(request, "Fill the form correctly!")
        return render(request,'merchant_add_products.html')


        # return render(request,'merchant_add_products.html')

def merchant_update_product(request,id):
    cont = product.objects.get(productId=id)
    context = { 'product_data' : product.objects.all().select_related('categoryName','subcategoryName','dietType'),'category':Categories.objects.all(),'subcategory':Sub_Categories.objects.all(),'diet':Diet.objects.all()}
    return render(request,'merchant_update_product.html',{'context': context,'cont': cont})

def editproduct(request,id):
    context = {}
    obj = get_object_or_404(product, productId=id)
    form = ProductForm(request.POST or None,request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Product updated successfully!")
        context['form'] = form
        return redirect("/merchant_manage_product",context)
    else:
        messages.error(request, "Failed to update Product!")
        return render(request,'merchant_update_product.html')

def deleteproduct(request,id):
    # context = {}
    obj = get_object_or_404(product,productId=id)
    if request.method == 'GET':
        obj.delete()
    
    messages.success(request, "Product deleted successfully!")
    if 'from_admin' in request.GET:
        return redirect("/admin_mng_products")
    else:
        return redirect("/merchant_manage_product")

def merchant_logout(request):
    try:
        del request.session['username'] 
        del request.session['email'] 
        del request.session['contact'] 
        del request.session['shopName'] 
        del request.session['shopAddr'] 
        del request.session['shopPhone'] 
        return render(request,'login.html')
    except Exception as e:
        return HttpResponse(e)
    return render(request,'merchant_login.html')

def merchant_profile(request):
    #context = { 'seller_data': seller_registration.objects.all()}
    return render(request,'merchant_profile.html')
    
    # if 'seller_reg' in request.session:
    #     current_user = request.session['seller_reg']
    #     param = {'current_user' : current_user}
    # else:
    #     return render(request,'merchant_login.html')

def merchant_profile_update(request):
    #context = seller_registration.objects.get(id=id)
    return render(request,'merchant_profile_update.html')

def merchant_profile_edit(request):
    if request.method == "POST":    
        em = request.POST.get("email1")
        #obj = seller_registration.objects.all()
        #obj = get_object_or_404(seller_registration)
        #check = check_password(em, obj.email)
        #obj = seller_registration()

        #if check == True:
        obj = merchant.objects.all()
        for i in range(len(obj)):
            if obj[i].email == em:
        
                obj.username = request.POST.get("username")
                obj.email = request.POST.get("email")
                obj.contact = request.POST.get("contact")
                obj.companyname = request.POST.get("companyname")
                obj.address = request.POST.get("address")
                obj.save()  
                messages.success(request, "Profile updated successfully!")
                return redirect("/merchant_profile")

    # form = SellerRegistrationForm(request.POST or None, instance=obj)
    # return HttpResponse(form)
    # try :
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Profile updated successfully!")
    #         context['form'] = form
    #         return redirect("/merchant_profile",context)
    # except:
    #     messages.error(request, "Failed to update profile!")
    #     return render(request,'merchant_profile_update.html')
    # return render(request,'merchant_profile_update.html')
        
def merchant_change_pswd(request):
    return render(request,'merchant_change_pswd.html')

def change_password(request):
    if request.method == "POST":    
        old_pswd = request.POST.get("password")
        username1 = request.POST.get("username1")
    
        obj = get_object_or_404(user, username = username1)
        
        result = check_password(old_pswd, obj.password)
        if obj.user_type == 2 and result == True:
            new_pswd = request.POST.get("new_password")
            cnfm_pswd = request.POST.get("cnfm_password")
            
            if new_pswd == cnfm_pswd:
                
                obj.password = make_password(new_pswd)
                obj.save()
                
                messages.success(request, "Password Changed successfully!")
                return render(request,'merchant_change_pswd.html')
            else :
                messages.error(request, "New Password and Confirm Password doesn't match!")
                return render(request, 'merchant_change_pswd.html')
        else:
            messages.error(request, "Old is password is not correct!")
            return render(request, 'merchant_change_pswd.html')
