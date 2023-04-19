from django import forms  
#from django.contrib.auth.models import UserCreationForm
#from django.db import forms
from administrator.models import Categories,Sub_Categories,Diet
from auth_app.models import user, merchant, customer
from merchant.models import product



class ProductForm(forms.ModelForm):  
    class Meta:  
        model = product
        fields = ('productId','productName','productQty','productPrice','productDesc','productImage','categoryName','subcategoryName','dietType',)