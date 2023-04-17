from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from auth_app.models import merchant
from auth_app.forms import merchantReg

# # Create your views here.
def merchant(request):
    return render(request,'merchant_index.html')

def merchant_add_products(request):
    return render(request,'merchant_add_products.html')

def merchant_logout(request):
    return render(request,'merchant_login.html')

def merchant_profile(request):
    context = { 'seller_data': merchant.objects.all()}
    return render(request,'merchant_profile.html',{'context': context})

def merchant_profile_update(request,id):
    context =  merchant.objects.get(id=id)
    return render(request,'merchant_profile_update.html',{'context': context})

def merchant_profile_edit(request,id):
    context = {}
    obj = get_object_or_404(merchant, id=id)
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
        