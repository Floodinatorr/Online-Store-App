from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

def ProductDetail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request,'product/product_detail.html',context)
