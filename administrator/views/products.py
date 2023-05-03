from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from auth_app.models import user, customer, merchant
from administrator.models import Categories,Sub_Categories,Diet
from merchant.models import product
from user.models import BillItems
from recipe.models import Recipe,RecipeIngredient
from recipe.forms import RecipeIngredientForm

from administrator.forms import SubCategoryForm,CategoryForm,DietForm
from django.core.paginator import Paginator
import csv
from reportlab.pdfgen import canvas
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

def admin_mng_products(request):
    # context={}
    obj = product.objects.all()
    return render(request,'admin_mng_products.html',{'context':obj})

# approve product
def toggle_product_approval(request, id):
    productVar = get_object_or_404(product, productId=id)
    productVar.isApproved = not productVar.isApproved
    productVar.save()
    # return HttpResponse(productVar.isApproved)
    return redirect('/admin_mng_products')

def admin_recipe(request):
    # return HttpResponse('successful') 
    rec = Recipe.objects.all()
    return render(request,'admin_recipe.html',context={'rec':rec})
    # return render(request,'admin_recipe.html')

def add_recipe(request):
    if request.method == "POST": 
        add_recipe = Recipe()
        add_recipe.recipe_name = request.POST.get('recipe_name')
        add_recipe.recipeDescription = request.POST.get('recipeDescription')
        
        
        add_recipe.save()
        messages.success(request, "Recipe added successfully!")
        rec = { 'rec': Recipe.objects.all()}

        return render(request,'admin_recipe.html',{'rec':rec})
    
def delete_recipe(request,id):
    context = {}
    obj = get_object_or_404(Recipe,recipe_id=id)
    if request.method == "GET":
        obj.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect("/admin-recipe")
    else:
        messages.error(request, "Failed to delete Recipe!")
        return render(request, "admin_recipe.html", context)
    
def admin_recipeIng(request):
    context = { 'recipe_data' : RecipeIngredient.objects.all().select_related('recipe','ingredient').order_by('id'),'recipes':Recipe.objects.all().order_by('recipe_id'),'products':product.objects.all().order_by('productId')}
    return render(request,'admin_recipeIng.html',{'context': context})
    
def add_recipeIng(request):  
    if request.method == "POST": 
        c_form = RecipeIngredientForm(request.POST or None)
        # s = request.POST.get('recipe')
        # d = request.POST.get('ingredient') 
        # f = request.POST.get('amount') 
        # g = request.POST.get('unit') 
        
        # return HttpResponse(f)
        if c_form.is_valid():
            c_form.save()
            messages.success(request, "Ingredients inserted successfully!")
            context = { 'RI_data': RecipeIngredient.objects.all()}
            return render(request,'admin_recipeIng.html',{'context': context})
        
        else:
            messages.error(request, "Ingredients insertion failed!")
            return render(request,'admin_recipeIng.html')
    else:
        messages.error(request, "Fill the form correctly!")
        return render(request,'admin_recipeIng.html')