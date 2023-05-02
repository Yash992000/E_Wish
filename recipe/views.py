from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from user.models import Bill, BillItems
from .models import Recipe, RecipeIngredient
from django.db.models import Q

def recipeView(request,id):
    # return HttpResponse(id)
    # billId = Bill.objects.get(BillId=billId)
    bill_items = BillItems.objects.filter(Bill_id_id=id)
    products = [item.productId for item in bill_items]
    
    recipes = Recipe.objects.filter(
        Q(recipeingredient__ingredient__in=products)
    ).distinct()

    context = {'recipes': recipes, 'id': id}
    return render(request, 'recipeView.html', context)    