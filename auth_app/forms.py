from django import forms
from auth_app.models import user, merchant, customer

class BasicReg(forms.ModelForm):
      class Meta:  
        model = user 
        fields = ('username','email','contact','image','password', 'user_type', 'isAdmin')

class customerReg(forms.ModelForm):
    class Meta:
        model = customer
        fields = ('userAddress','city','state')

class merchantReg(forms.ModelForm):
    class Meta:
        model = merchant
        fields = ('shopName', 'shopAddr', 'shopPhone', 'shopCity', 'shopState')

# class UserRegistrationForm(forms.ModelForm):  
#     class Meta:  
#         model = user_registration 
#         fields = ('username','email','contact','address','image','password',)

# class SellerRegistrationForm(forms.ModelForm):  
#     class Meta:  
#         model = seller_registration 
#         fields = ('username','email','contact','companyname','address','image','password',)

# class AdminRegistrationForm(forms.ModelForm):  
#     class Meta:  
#         model = admin_registration 
#         fields = ('email','password',)