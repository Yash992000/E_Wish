from django import forms
from user.models import Contact

class ContactForm(forms.ModelForm):
      class Meta:  
        model = Contact 
        fields = ('name','email','number','message')