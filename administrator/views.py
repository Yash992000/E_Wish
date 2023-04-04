from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from auth_app.models import user_registration,seller_registration, admin_registration
from administrator.models import Categories,Sub_Categories
from administrator.forms import SubCategoryForm  
# from Login.models import SignUp  

# Create your views here.
def admin(request):
    return render(request,'admin_index.html')

def admin_categories(request):
    context = { 'category_data': Categories.objects.all()}
    return render(request,'admin_categories.html',{'context': context})

def admin_subcategories(request):
    context = { 'subcategory_data': Sub_Categories.objects.all().select_related('categoryName').order_by('-subcategoryId'), 'category': Categories.objects.all().order_by('-categoryId')}
    return render(request,'admin_subcategories.html',{'context': context})

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

def add_category(request):  
    if request.method == "POST": 
        add_cat = Categories()
        add_cat.categoryName = request.POST.get('categoryName')
        if Categories.objects.filter(categoryName=add_cat.categoryName).exists():
            return render(request,"admin_categories.html") 
        
        if len(request.FILES) != 0:
            add_cat.categoryImage = request.FILES['categoryImage']
        
        add_cat.save()
        context = { 'category_data': Categories.objects.all()}
        return render(request,'admin_categories.html',{'context': context})

        # return render (request, "admin_categories.html")
    return HttpResponse('Fail')

def deletecategory(request,id):
    context = {}
    obj = get_object_or_404(Categories,categoryId=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/admin_categories")
    return render(request, "admin_categories.html", context)

def add_subcategory(request):  
    if request.method == "POST": 
        c_form = SubCategoryForm(request.POST or None, request.FILES) 

        if c_form.is_valid():
            
            c_form.save()
        context = { 'category_data': Sub_Categories.objects.all()}
        return render(request,'admin_subcategories.html',{'context': context})

    return HttpResponse('Fail')

def deletesubcategory(request,id):
    context = {}
    obj = get_object_or_404(Sub_Categories,subcategoryId=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/admin_subcategories")
    return render(request, "admin_subcategories.html", context)