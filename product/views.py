from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from product.models import Product
from product.forms import ProductForm 
from django.contrib import messages
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView
)

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
            messages.success(request,"Your product saved successfully.")
            #return JsonResponse({'message': 'Product created successfully'})
        else:
            messages.error(request,"Something went wrong.")
        

    return render(request,'product/product.html',context={'product_form': product_form})


def product_list(request):
    products =  Product.objects.all()
    # print(products.query)
    return render(request, 'product/product_list.html', context={"products":products})

def product_update_view(request,pk):
    product = Product.objects.get(id=pk)
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

    # product_form = ProductForm()
    if request.method == "POST":
            product_form = ProductForm(request.POST, request.FILES, instance=product)
    
            if product_form.is_valid():
                product_form.save()
                messages.success(request,"Your product saved successfully.")
                #return JsonResponse({'message': 'Product created successfully'})
            else:
                messages.error(request,"Something went wrong.")
    else:
        product_form = ProductForm(instance=product)        
    
    return render(request,'product/product.html',context={"product_form":product_form})


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = "products"

class ProductCreateView(CreateView):
    model = Product
    template_name = "product/product.html"
    form_class = ProductForm
    success_url = "/product"

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "product/product.html"
    form_class = ProductForm
    success_url = "/product"