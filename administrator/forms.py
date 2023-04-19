from django import forms  
#from django.contrib.auth.models import UserCreationForm
#from django.db import forms
from administrator.models import Categories,Sub_Categories,Diet
 
class CategoryForm(forms.ModelForm):  
    class Meta:  
        model = Categories 
        fields = ('categoryId','categoryName','categoryImage',)

class SubCategoryForm(forms.ModelForm):  
    class Meta:  
        model = Sub_Categories 
        fields = ('subcategoryId','subcategoryName','subcategoryImage','categoryName',)

class DietForm(forms.ModelForm):  
    class Meta:  
        model = Diet 
        fields = ('dietId','dietType','dietDisc',)
