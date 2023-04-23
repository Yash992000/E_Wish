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
# from Login.models import SignUp  

# Create your views here.
def admin(request):
    return render(request,'admin_index.html')

def admin_categories(request):
    category = Categories.objects.all()
    p = Paginator(category, 3)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)                   
    return render(request,'admin_categories.html', context={"category":page_obj}) # calls category page

def admin_subcategories(request):
    context = { 'subcategory_data': Sub_Categories.objects.all().select_related('categoryName').order_by('subcategoryId'), 'category': Categories.objects.all().order_by('categoryId')}
    return render(request,'admin_subcategories.html',{'context': context})

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

def admin_mng_products(request):
    # context={}
    obj = product.objects.all()
    return render(request,'admin_mng_products.html',{'context':obj})

def admin_feedback(request):
    return render(request,'admin_feedback.html')

def admin_mng_users(request):
    user1 = user.objects.all()
    p = Paginator(user1, 5)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)                   
    return render(request,'admin_mng_users.html', context={"userdata":page_obj}) # calls category page

def admin_mng_merchant(request):
    userProfile = user.objects.all()
    seller = merchant.objects.all()
    
    # merchUsers = user.objects.filter(user_type = 2)
    merchData = merchant.objects.filter(UserId__user_type = 2)
    
    p = Paginator(merchData, 5)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)                   
    return render(request,'admin_mng_merchant.html', context={"merchData":page_obj}) # calls category page

def admin_mng_customer(request):
    userProfile = user.objects.all()
    custom = customer.objects.all()
    
    # merchUsers = user.objects.filter(user_type = 2)
    custData = customer.objects.filter(UserId__user_type = 1)
    
    p = Paginator(custData, 5)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)                   
    return render(request,'admin_mng_customer.html', context={"custData":page_obj}) # calls category page

def deleteuser(request,id):
    context = {}
    obj = get_object_or_404(user,UserId=id)
    if obj.user_type == 1:
        cust = get_object_or_404(customer, UserId = id)
        if request.method == "GET":
            cust.delete()
    elif obj.user_type == 2:
        merch = get_object_or_404(merchant, UserId = id)  
        if request.method == "GET":
            merch.delete()
    
    if request.method == "GET":
        obj.delete()
        messages.success(request, "User deleted successfully!")
        return redirect("/admin_mng_users")
    else:
        messages.error(request, "Failed to delete user!")
        return render(request, "admin_mng_users.html", context)

def deleteseller(request,id):
    context = {}
    obj = get_object_or_404(merchant,MerchId=id)
    obj2 = get_object_or_404(user, UserId=obj.UserId.UserId)
    if request.method == "GET":
        obj2.user_type = 3
        obj2.save()
        obj.delete()
        messages.success(request, "Seller deleted successfully!")
        return redirect("/admin_mng_merchant")
    else:
        messages.error(request, "Failed to delete seller!")
        return render(request, "admin_mng_merchant.html", context)
    
def deletecustomer(request,id):
    context = {}
    obj = get_object_or_404(customer,CustomerId=id)
    obj2 = get_object_or_404(user, UserId=obj.UserId.UserId)
    if request.method == "GET":
        obj2.user_type = 3
        obj2.save()
        obj.delete()
        messages.success(request, "Customer deleted successfully!")
        return redirect("/admin_mng_customer")
    else:
        messages.error(request, "Failed to delete Customer!")
        return render(request, "admin_mng_customer.html", context)

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
        category = Categories.objects.all()
        return render(request,'admin_categories.html', context={"category":category}) # calls category page

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
    cont = Sub_Categories.objects.get(subcategoryId=id)
    context = { 'subcategory_data': Sub_Categories.objects.all().select_related('categoryName'), 'category': Categories.objects.all()}
    return render(request,'admin_update_subcategories.html',{'cont':cont,'context':context})
    
def editSubCategory(request,id):
    context = {}
    obj = get_object_or_404(Sub_Categories, subcategoryId=id)
    form = SubCategoryForm(request.POST or None,request.FILES, instance=obj)
    # return HttpResponse(form)
    if form.is_valid():
        form.save()
        messages.success(request, "Sub-Category updated successfully!")
        context['form'] = form
        return redirect("/admin_subcategories",context)
    else:
        messages.error(request, "Failed to update Sub-Category!")
        return render(request,'admin_subcategories.html')

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
    
def admin_logout(request):
    return render(request,'admin_login.html')
#==========================================================================================================
# Download code:
def downloadCat(request):
    download_type = request.POST.get('download-type')

    if download_type == 'excel':
        response = HttpResponse('text/csv')
        response['Content-Disposition'] = 'attachment; filename="Categories.csv"'

        writer = csv.writer(response)
        writer.writerow(['category_id','category_name',"category_image"])
        for data in Categories.objects.all():
            writer.writerow([data.categoryId, data.categoryName, data.categoryImage])

        return response
    elif download_type == 'pdf':
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Categories.pdf"'

        # Create a new PDF document and write to the response
        pdf = canvas.Canvas(response)
        pdf.setTitle("Categories Report")

        # Define the table headers
        headers = ['Category ID', 'Category Name']

        # Define the table data
        data = [[c.categoryId, c.categoryName] for c in Categories.objects.all()]

        # Define the width and height of each column
        col_widths = [pdf.stringWidth(h) + 10 for h in headers]
        row_height = 20

        # Draw the table headers
        for i, header in enumerate(headers):
            pdf.drawString(sum(col_widths[:i]), 750, header)

        # Draw the table data
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                pdf.drawString(sum(col_widths[:j]), 720 - (i + 1) * row_height, str(cell))

        # Save the PDF document and close the canvas
        pdf.save()

        return response


def downloadDiet(request):
    download_type = request.POST.get('download-type')
    
    if download_type == 'excel':
        response=HttpResponse('txt/csv')
        response['content-Disposition'] = 'attachment; filename=Diets.csv'
        writer = csv.writer(response)
        writer.writerow(['Diet ID','Diet Name',"Diet Description"])
        for data in Diet.objects.all():
            writer.writerow([data.dietId, data.dietType, data.dietDisc])
    
    elif download_type == 'pdf':
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Diets.pdf"'

        # Create a new PDF document and write to the response
        pdf = canvas.Canvas(response)
        pdf.setTitle("Diets Report")

        # Define the table headers
        headers = ['Diet ID', 'Diet Name', 'Diet Description']

        # Define the table data
        data = [[d.dietId, d.dietType, d.dietDisc] for d in Diet.objects.all()]

        # Define the width and height of each column
        col_widths = [pdf.stringWidth(h) + 10 for h in headers]
        row_height = 20

        # Draw the table headers
        for i, header in enumerate(headers):
            pdf.drawString(sum(col_widths[:i]), 750, header)

        # Draw the table data
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                pdf.drawString(sum(col_widths[:j]), 720 - (i + 1) * row_height, str(cell))

        # Save the PDF document and close the canvas
        pdf.save()
        
    return response

def downloadSubCat(request):
    download_type = request.POST.get('download-type')

    if download_type == 'excel':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Subcategories.csv"'

        writer = csv.writer(response)
        writer.writerow(['Subcategory ID', 'Subcategory Name', 'Category Name', 'Subcategory Image'])
        for data in Sub_Categories.objects.all():
            writer.writerow([data.subcategoryId, data.subcategoryName, data.categoryName, data.subcategoryImage])

        return response

    elif download_type == 'pdf':
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Subcategories.pdf"'

        # Create a new PDF document and write to the response
        pdf = canvas.Canvas(response)
        pdf.setTitle("Subcategories Report")

        # Define the table headers
        headers = ['Subcategory ID', 'Subcategory Name', 'Category Name']

        # Define the table data
        data = [[s.subcategoryId, s.subcategoryName, s.categoryName] for s in Sub_Categories.objects.all()]

        # Define the width and height of each column
        col_widths = [pdf.stringWidth(h) + 10 for h in headers]
        row_height = 20

        # Draw the table headers
        for i, header in enumerate(headers):
            pdf.drawString(sum(col_widths[:i]), 750, header)

        # Draw the table data
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                pdf.drawString(sum(col_widths[:j]), 720 - (i + 1) * row_height, str(cell))

        # Save the PDF document and close the canvas
        pdf.save()

        return response

def downloadProduct(request):
    download_type = request.POST.get('download-type')
    
    if download_type == 'excel':
        response=HttpResponse('txt/csv')
        response['content-Disposition'] = 'attachment; filename=Products.csv'
        writer = csv.writer(response)
        writer.writerow(['Product Id','Product Name','Category Name', 'Sub category name', 'Product description', 'Product price', 'Available quantity', 'Serving size', 'Diet type', 'Approved', 'Product Image'])
        for data in product.objects.all():
            writer.writerow([data.productId, data.productName, data.categoryName, data.subcategoryName, data.productPrice, data.productQty, data.productServing, data.dietType, data.isApproved, data.productImage])

        return response
    elif download_type == 'pdf':
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Products.pdf"'

        # Create a new PDF document and write to the response
        pdf = canvas.Canvas(response)
        pdf.setTitle("Products Report")

        # Define the table headers
        headers = ['Product Id','Product Name','Category Name', 'Sub category name', 'Product description', 'Product price', 'Available quantity', 'Serving size', 'Diet type', 'Approved']

        # Define the table data
        data = [[p.productId, p.productName, p.categoryName, p.subcategoryName, p.productPrice, p.productQty, p.productServing, p.dietType, p.isApproved] for p in product.objects.all()]

        # Define the width and height of each column
        col_widths = [pdf.stringWidth(h) + 10 for h in headers]
        row_height = 20

        # Draw the table headers
        for i, header in enumerate(headers):
            pdf.drawString(sum(col_widths[:i]), 750, header)

        # Draw the table data
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                pdf.drawString(sum(col_widths[:j]), 720 - (i + 1) * row_height, str(cell))

        # Save the PDF document and close the canvas
        pdf.save()
        
        return response

def downloadUser(request): 
    download_type = request.POST.get('download-type')
    
    if download_type == 'excel':
        response=HttpResponse('txt/csv')
        response['content-Disposition'] = 'attachment; filename=Users.csv'
        writer = csv.writer(response)
        writer.writerow(['User ID', 'User Name', 'User Phone', 'User Email', 'User Password (encrypted)', 'User Type', 'User Image', 'Is Admin'])
        for data in user.objects.all():
            writer.writerow([data.UserId, data.username, data.contact, data.email, data.password, data.user_type, data.image, data.isAdmin])

        return response
    elif download_type == 'pdf':
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Users.pdf"'

        # Create a new PDF document and write to the response
        pdf = canvas.Canvas(response)
        pdf.setTitle("Users Report")

        # Define the table headers
        headers = ['User ID', 'User Name', 'User Phone', 'User Email', 'User Type', 'Is Admin']

        # Define the table data
        data = [[u.UserId, u.username, u.contact, u.email, u.user_type, u.isAdmin] for u in user.objects.all()]

        # Define the width and height of each column
        col_widths = [pdf.stringWidth(h) + 10 for h in headers]
        row_height = 20

        # Draw the table headers
        for i, header in enumerate(headers):
            pdf.drawString(sum(col_widths[:i]), 750, header)

        # Draw the table data
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                pdf.drawString(sum(col_widths[:j]), 720 - (i + 1) * row_height, str(cell))

        # Save the PDF document and close the canvas
        pdf.save()
        
        return response

# approve product
def toggle_product_approval(request, id):
    productVar = get_object_or_404(product, productId=id)
    productVar.isApproved = not productVar.isApproved
    productVar.save()
    # return HttpResponse(productVar.isApproved)
    return redirect('/admin_mng_products')