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