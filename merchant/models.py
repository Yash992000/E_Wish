from django.db import models
from administrator.models import Categories,Sub_Categories,Diet
from auth_app.models import user


# Create your models here.
class product(models.Model):
    productId = models.AutoField(primary_key = True)
    categoryName = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategoryName = models.ForeignKey(Sub_Categories, on_delete=models.CASCADE)
    dietType = models.ForeignKey(Diet, on_delete=models.CASCADE)
    productName = models.TextField(max_length=500)
    productQty = models.TextField(max_length=500)
    productPrice = models.TextField(max_length=500)
    productDesc = models.TextField(max_length=500)
    productImage = models.ImageField(upload_to='product/image',null=True,blank=True)


    def __str__(self):
        return self.ProductId

