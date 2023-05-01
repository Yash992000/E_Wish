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
from django.db.models import Count

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
        deit = Diet.objects.all()
        return render(request,'admin_dietary_preferance.html', context={"deit":deit}) # calls category page

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

# bulk upload:

def bulk_upload(request):
    if request.method == 'GET':
        return render(request, "bulkUpload.html")
    
    csv_file = request.FILES['csv_file']
    if not csv_file.name.endswith('.csv'):
        return HttpResponse("File not valid")
    if csv_file.multiple_chunks():
        return HttpResponse("Uploaded file is big")
    
    file_data = csv_file.read().decode("UTF-8")
    lines = file_data.split("\n")
    c = len(lines)
    for i in range(0, c-1):
        fields = lines[i].split(",")
        data_dict = {}
        data_dict["dietType"] = fields[0]
        data_dict["dietDisc"] = fields[1]
        
        form = DietForm(data_dict)
        if form.is_valid():
            form.save()
    
    return redirect("/admin_dietary_preferance")

def pie_chart(request):
    diets = Diet.objects.annotate(product_count=Count('product'))
    diet_labels = [diet.dietType for diet in diets]
    product_counts = [diet.product_count for diet in diets]
    return render(request, 'pie_chart.html', {'diet_labels': diet_labels, 'product_counts': product_counts})