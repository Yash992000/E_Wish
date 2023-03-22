from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from auth_app.models import user_registration,seller_registration, admin_registration
# from Login.forms import SignUpForm  
# from Login.models import SignUp  

# Create your views here.
def admin(request):
    return render(request,'admin_index.html')

def admin_categories(request):
    return render(request,'admin_categories.html')

def admin_subcategories(request):
    return render(request,'admin_subcategories.html')

def admin_mng_products(request):
    return render(request,'admin_mng_products.html')

def admin_feedback(request):
    return render(request,'admin_feedback.html')

def admin_mng_users(request):
    context = { 'user_data': user_registration.objects.all() }
    return render(request,'admin_mng_users.html',{'context': context})

def admin_mng_merchant(request):
    context = { 'seller_data': seller_registration.objects.all() }
    return render(request,'admin_mng_merchant.html',{'context': context})

def deleteuser(request,id):
    context = {}
    obj = get_object_or_404(user_registration,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/admin_mng_users")
    return render(request, "admin_mng_users.html", context)

def deleteseller(request,id):
    context = {}
    obj = get_object_or_404(seller_registration,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/admin_mng_merchant")
    return render(request, "admin_mng_merchant.html", context)