from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from auth_app.models import user_registration,seller_registration, admin_registration
from administrator.models import Categories,Sub_Categories
from administrator.forms import SubCategoryForm,CategoryForm
# from Login.models import SignUp  

# Create your views here.
def admin(request):
    return render(request,'admin_index.html')

def admin_categories(request):
    context = { 'category_data': Categories.objects.all()}
    return render(request,'admin_categories.html',{'context': context})

def admin_subcategories(request):
    context = { 'subcategory_data': Sub_Categories.objects.all().select_related('categoryName').order_by('subcategoryId'), 'category': Categories.objects.all().order_by('categoryId')}
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
        messages.success(request, "User deleted successfully!")
        return redirect("/admin_mng_users")
    else:
        messages.error(request, "Failed to delete user!")
        return render(request, "admin_mng_users.html", context)

def deleteseller(request,id):
    context = {}
    obj = get_object_or_404(seller_registration,id=id)
    if request.method == "GET":
        obj.delete()
        messages.success(request, "Seller deleted successfully!")
        return redirect("/admin_mng_merchant")
    else:
        messages.error(request, "Failed to delete seller!")
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
        messages.success(request, "Category added successfully!")
        context = { 'category_data': Categories.objects.all()}
        return render(request,'admin_categories.html',{'context': context})

    else:
        messages.error(request, "Category insertion failed!")
        return render (request, "admin_categories.html")


def deletecategory(request,id):
    context = {}
    obj = get_object_or_404(Categories,categoryId=id)
    if request.method == "GET":
        obj.delete()
        messages.success(request, "Category deleted successfully!")
        return redirect("/admin_categories")
    else:
        messages.error(request, "Failed to delete category!")
        return render(request, "admin_categories.html", context)

def admin_update_categories(request,id):
    context = Categories.objects.get(categoryId=id)
    return render(request,'admin_update_categories.html',{'context': context})

def editCategory(request,id):
    context = {}
    obj = get_object_or_404(Categories, categoryId=id)
    form = CategoryForm(request.POST or None,request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Category updated successfully!")
        context['form'] = form
        return redirect("/admin_categories",context)
    else:
        messages.error(request, "Failed to update category!")
        return render(request,'admin_categories.html')
    

def add_subcategory(request):  
    if request.method == "POST": 
        c_form = SubCategoryForm(request.POST or None, request.FILES) 
        if c_form.is_valid():
            c_form.save()
            messages.success(request, "Sub-Category inserted successfully!")
            context = { 'subcategory_data': Sub_Categories.objects.all()}
            return render(request,'admin_subcategories.html',{'context': context})
        
        else:
            messages.error(request, "Sub-category insertion failed!")
            return render(request,'admin_subcategories.html')
    else:
        messages.error(request, "Fill the form correctly!")
        return render(request,'admin_subcategories.html')

def deletesubcategory(request,id):
    context = {}
    obj = get_object_or_404(Sub_Categories,subcategoryId=id)
    if request.method == "GET":
        obj.delete()
        messages.success(request, "Sub-Category deleted successfully!")
        return redirect("/admin_subcategories")
    else:
        messages.error(request, "Failed to delete Sub-Category!")
        return render(request, "admin_subcategories.html", context)

def admin_update_subcategories(request,id):
    context = Sub_Categories.objects.get(subcategoryId=id)
    return render(request,'admin_update_subcategories.html',{'context': context})
    
    #context = { 'subcategory_data': Sub_Categories.objects.get(subcategoryId=id).select_related('categoryName').order_by('-subcategoryId'), 'category': Categories.objects.all().order_by('-categoryId')}

# def admin_subcategories(request):
#     context = { 'subcategory_data': Sub_Categories.objects.all().select_related('categoryName').order_by('-subcategoryId'), 'category': Categories.objects.all().order_by('-categoryId')}
#     return render(request,'admin_subcategories.html',{'context': context})

def editSubCategory(request,id):
    context = {}
    obj = get_object_or_404(Sub_Categories, subcategoryId=id)
    form = SubCategoryForm(request.POST or None,request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Sub-Category updated successfully!")
        context['form'] = form
        return redirect("/admin_subcategories",context)
    else:
        messages.error(request, "Failed to update Sub-Category!")
        return render(request,'admin_subcategories.html')

def admin_logout(request):
    return render(request,'admin_login.html')

