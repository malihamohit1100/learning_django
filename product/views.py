from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from product.models import Product,Customer,Address,Category
from product.forms import ProductForm 
from django.contrib import messages
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView
)
from django.contrib.auth.models import User
from django.db.models import Q,Sum,Avg,Count

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

def test_view(request):
    # users = User.objects.all()
    products = Product.objects.all().select_related('category') # one to one field, foreign key te kaj kore select keyword
    # print(products.query)

    # foregnkey, one to one --> select_related
    # reverse foregnkey, many to many --> prefetch_related

    # checked different ORM QUERIES

    # print(users)
    # products = Product.objects.values('product_name', 'product_price')
    # product = Product.objects.get(id=13)
    # print(product.category)
    # products = Product.objects.values('product_name').distinct()
    # print(products)
    # products = Product.objects.filter(product_name = "Laptop", product_price__gte ="100")
    # print(products)
    # products = Product.objects.filter(
    #     Q(product_name = "Laptop") & (Q(product_price__gt ="100") | 
    #     Q(product_price__lte ="100"))
    # )
    # print(products)
    # products = Product.objects.all().order_by('-product_price')
    # for product in products:
    #     print(product.product_price)
    # product_price = Product.objects.aggregate(Total_price=Sum('product_price'))
    # print(product_price)
    # products = Product.objects.annotate( #didn't work, couldn't create the extra column total_product
    #     total_product = Count('product_name')
    # )
    # print(products.values)
    # for product in products: #1query (N+1)
        # print(product.product_name)
        # print(product.product_price)
        # print(product.category) #N query (product number = query number)
    category = Category.objects.get(id=1)
    print(category.products.all())

    # return HttpResponse("<h1>Test View</h1>")
    return render(request=request,template_name='debug.html')