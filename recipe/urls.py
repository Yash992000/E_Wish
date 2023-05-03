from django.urls import path
from . import views

urlpatterns = [
    path('recipeView<id>',views.recipeView, name="recipeView"),    
]