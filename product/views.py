from django.shortcuts import render

# Create your views here.
# view can be a function or class based view

def product_view(request):
    print('Hitting product view')
    return render(request, 'product/product.html' )
