from django import forms  
#from django.contrib.auth.models import UserCreationForm
#from django.db import forms

from merchant.models import product


class ProductForm(forms.ModelForm):  
    class Meta:  
        model = product
        fields = ('productId','productName','productQty','productPrice','productDesc','productImage','categoryName','subcategoryName','dietType','productServing',)