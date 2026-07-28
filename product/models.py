from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_slug = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):#child
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(
        to=Category,#parent
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='products'
    )
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField(null=True, blank=True)
    product_image = models.ImageField(upload_to='images', null=True, blank=True)
    quantity = models.IntegerField(null=True,blank=True,default=1)

    def __str__(self):
        return self.product_name

class Address(models.Model):
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)

    def __str__(self):
        return self.region

class Customer(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    address = models.ManyToManyField(to=Address)

    def __str__(self):
        return self.user.first_name