from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField(null=True, blank=True)
    product_image = models.ImageField(upload_to='images', null=True, blank=True)