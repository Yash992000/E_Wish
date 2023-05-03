from django import forms  
#from django.contrib.auth.models import UserCreationForm
#from django.db import forms

from recipe.models import RecipeIngredient


class RecipeIngredientForm(forms.ModelForm):  
    class Meta:  
        model = RecipeIngredient
        fields = ('recipe','ingredient','amount','unit')