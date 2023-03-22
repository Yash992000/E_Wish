from django import forms  
#from django.contrib.auth.models import UserCreationForm
#from django.db import forms
from auth_app.models import user_registration, seller_registration, admin_registration
 
class UserRegistrationForm(forms.ModelForm):  
    class Meta:  
        model = user_registration 
        fields = ('username','email','contact','address','image','password',)

class SellerRegistrationForm(forms.ModelForm):  
    class Meta:  
        model = seller_registration 
        fields = ('username','email','contact','companyname','address','image','password',)

class AdminRegistrationForm(forms.ModelForm):  
    class Meta:  
        model = admin_registration 
        fields = ('email','password',)