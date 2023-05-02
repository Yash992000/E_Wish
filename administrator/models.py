from django.db import models
#from merchant.models import product

# Create your models here.
class Categories(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.TextField(unique=True,blank = True, max_length=50)
    categoryImage = models.ImageField(upload_to='administrator/image',null=True,blank=True)

class Sub_Categories(models.Model):
    subcategoryId = models.AutoField(primary_key=True)
    subcategoryName = models.TextField(unique=True,blank = True, max_length=50)
    subcategoryImage = models.ImageField(upload_to='administrator/image',null=True,blank=True)
    categoryName = models.ForeignKey(Categories, on_delete=models.CASCADE,related_name='category')

class Diet(models.Model):
    dietId = models.AutoField(primary_key=True)
    dietType = models.TextField(unique=True,blank = True, max_length=50)
    dietDisc = models.TextField(blank = True, max_length=500)
    
    def __str__(self):
        return self.dietType

# # recipe

# class Recipe(models.Model):
#     recipe_id = models.AutoField(primary_key=True)
#     recipe_name = models.CharField(max_length=255)

#     def _str_(self):
#         return self.recipe_name

# class RecipeIngredient(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     unit = models.CharField(max_length=20)

#     class Meta:
#         unique_together = ('recipe', 'ingredient')

#     def _str_(self):
#         return f"{self.amount} {self.unit} of {self.ingredient} for {self.recipe}"