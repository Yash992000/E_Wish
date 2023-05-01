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

def admin_dietary_preference(request):
    diet = Diet.objects.all()
    p = Paginator(diet, 5)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)                   
    return render(request,'admin_dietary_preferance.html', context={"diet":page_obj}) # calls category page

def admin_feedback(request):
    return render(request,'admin_feedback.html')

def add_dietary(request):  
    if request.method == "POST": 
        add_diet = Diet()
        add_diet.dietType = request.POST.get('dietType')
        if Diet.objects.filter(dietType=add_diet.dietType).exists():
            return render(request,"admin_dietary_preferance.html") 
        add_diet.dietDisc = request.POST.get('dietDisc')
        
        
        add_diet.save()
        messages.success(request, "Diet added successfully!")
        deit = { 'diet': Diet.objects.all()}

        #deit = Diet.objects.all()
        return render(request,'admin_dietary_preferance.html',{'deit':deit}) # calls category page

    else:
        messages.error(request, "Diet insertion failed!")
        return render (request, "admin_dietary_preferance.html")
    
def deletediet(request,id):
    context = {}
    obj = get_object_or_404(Diet,dietId=id)
    if request.method == "GET":
        obj.delete()
        messages.success(request, "Diet Type deleted successfully!")
        return redirect("/admin_dietary_preference")
    else:
        messages.error(request, "Failed to delete record!")
        return render(request, "admin_dietary_preferance.html", context)

def admin_update_diet(request,id):
    context = Diet.objects.get(dietId=id)
    return render(request,'admin_update_diet.html',{'context': context})

def editDiet(request,id):
    context = {}
    obj = get_object_or_404(Diet, dietId=id)
    form = DietForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Diet updated successfully!")
        context['form'] = form
        return redirect("/admin_dietary_preference",context)
    else:
        messages.error(request, "Failed to update diet!")
        return render(request,'admin_dietary_preferance.html')
