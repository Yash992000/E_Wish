from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from auth_app.models import merchant
from auth_app.forms import merchantReg

# # Create your views here.
def merchant_index(request):
    return render(request,'merchant_index.html')

def merchant_add_products(request):
    return render(request,'merchant_add_products.html')

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
        