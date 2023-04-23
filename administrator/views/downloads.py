from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from auth_app.models import user
from administrator.models import Categories,Sub_Categories,Diet
from merchant.models import product
import csv
from reportlab.pdfgen import canvas

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
