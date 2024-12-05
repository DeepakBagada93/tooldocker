from django.shortcuts import render,get_object_or_404
from .models import Product

def home(request):
    return render(request, 'shop/home.html')

def aboutus(request):
    return render(request, 'shop/aboutus.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})