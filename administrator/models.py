# from django.db import models

# # Create your models here.
# class Categories(models.Model):
#     categoryId = models.AutoField(primary_key=True)
#     categoryName = models.TextField(unique=True,blank = True, max_length=50)
#     categoryImage = models.ImageField(upload_to='administrator/image',null=True,blank=True)

# class Sub_Categories(models.Model):
#     subcategoryId = models.AutoField(primary_key=True)
#     subcategoryName = models.TextField(unique=True,blank = True, max_length=50)
#     subcategoryImage = models.ImageField(upload_to='administrator/image',null=True,blank=True)
#     categoryName = models.ForeignKey(Categories, on_delete=models.CASCADE,related_name='category')
