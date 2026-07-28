from django.contrib import admin
from .models import Product, Address, Category, Customer

# Register your models here.
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Customer)