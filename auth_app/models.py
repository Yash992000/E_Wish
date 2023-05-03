from django.db import models
from django.contrib.auth.hashers import make_password  

class user(models.Model):
    UserId = models.AutoField(primary_key = True)
    username = models.TextField(unique=True,max_length = 50)
    email = models.EmailField(unique=True,blank = True,max_length=50)
    contact = models.TextField(max_length = 10)
    # address = models.TextField(max_length = 100)
    image = models.ImageField(upload_to='auth_app/static/user_profile',null=True,blank=True)
    password = models.TextField(max_length = 50)
    user_type = models.IntegerField(blank = False)  # 1 is customer, 2 is merchant, 3 is undefinded.
    isAdmin = models.IntegerField(blank=False, default=0)
    # def save(self, *args, **kwargs):
    #     self.password = make_password(self.password)
    #     super(user,self).save(*args, **kwargs)

class customer(models.Model):
    UserId = models.ForeignKey(user, on_delete=models.CASCADE)
    CustomerId = models.AutoField(primary_key=True)
    userAddress = models.TextField(max_length=500)
    city = models.CharField(max_length=30, default="Ahmedabad")
    state = models.CharField(max_length=30, default = "Gujarat")
    def __str__(self):
        return self.CustomerId

class merchant(models.Model):
    UserId = models.ForeignKey(user, on_delete=models.CASCADE)
    MerchId = models.AutoField(primary_key=True)
    shopName = models.TextField(max_length=50)
    shopCity = models.CharField(max_length=30, default="Ahmedabad")
    shopState = models.CharField(max_length=30, default = "Gujarat")
    shopAddr = models.TextField(max_length=500)
    shopPhone = models.TextField(max_length=10)
    def __str__(self):
        return self.MerchId 