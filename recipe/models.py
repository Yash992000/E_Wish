from django.db import models
from merchant.models import product
# Create your models here.
# # recipe

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=255)
    recipeDescription = models.TextField(max_length=255)
    def _str_(self):
        return self.recipe_name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)

    class Meta:
        unique_together = ('recipe', 'ingredient')

    def _str_(self):
        return f"{self.amount} {self.unit} of {self.ingredient} for {self.recipe}"