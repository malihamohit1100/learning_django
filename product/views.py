from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from product.models import Product
from product.forms import ProductForm 

# Create your views here.
# view can be a function or class based view

def product_view(request):
    # data = request.POST
    # product_name = data.get('product_name')
    # product_price = data.get('product_price')
    # product_description = data.get('product_description')

    # product = Product(
    #     product_name = product_name,
    #     product_price = product_price,
    #     product_description = product_description
    # )

    # product.save()
    
    product_form = ProductForm()
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)

        if product_form.is_valid():
            product_form.save()
            #return JsonResponse({'message': 'Product created successfully'})
        

    return render(request,'product/product.html',context={'product_form': product_form})
