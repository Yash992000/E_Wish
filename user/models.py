from django.db import models
from auth_app.models import user
from merchant.models import product

# Create your models here.
class Cart(models.Model):
    UserId = models.ForeignKey(user, on_delete=models.CASCADE)
    cart_id = models.AutoField(primary_key=True, editable=False)
    completed = models.BooleanField(default=False)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product =  models.ForeignKey(product, on_delete=models.CASCADE)
    
class Bill(models.Model):
    BillId = models.AutoField(primary_key=True, editable=False)
    UserId = models.ForeignKey(user, on_delete=models.CASCADE)
    total_price = models.IntegerField(null=False)
       
class BillItems(models.Model):
    BillItemId = models.AutoField(primary_key=True, editable=False)
    Bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    cart =  models.ForeignKey(Cart, on_delete=models.CASCADE)
    # productQty = models.IntegerField(null=False)