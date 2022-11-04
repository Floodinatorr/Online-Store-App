from django.shortcuts import render, get_object_or_404
from .models import *
from products.models import Product
from django.http import HttpResponse

def CartAdd(request, id, count):
    product = Product.objects.get(id=id)
    if CartList.objects.get_queryset().filter(user=request.user).exists():
        cart = CartList.objects.get(user=request.user)
        if CartProductCount.objects.get_queryset().filter(cart=cart, product=product).exists():
            cart_product = CartProductCount.objects.get(cart=cart, product=product)
            cart_product.count += count
            cart_product.save()
        else:
            cart_product = CartProductCount.objects.create(cart=cart, product=product, count=count)
            cart_product.save()
        cart.products.add(product)
        cart.save()
        return HttpResponse("asdasdasd")
    else:
        cart = CartList.objects.create(user=request.user)
        return HttpResponse("Cart is empty")    
    
