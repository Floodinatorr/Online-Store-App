"""from django.shortcuts import render, get_object_or_404
from .models import *
from products.models import Product
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/login/')
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
    else:
        cart = CartList.objects.create(user=request.user)
        cart_product = CartProductCount.objects.create(cart=cart, product=product, count=count)
        cart_product.save()
        cart.products.add(product)
        cart.save()
    return HttpResponse('{"status": "added_cart"}', content_type='text/json')  
"""

from rest_framework import viewsets
from .serializers import *
from .models import *

class CartListViewSet(viewsets.ModelViewSet):
    queryset = CartList.objects.all()
    serializer_class = CartListSerializer

class CartProductCountViewSet(viewsets.ModelViewSet):
    queryset = CartProductCount.objects.all()
    serializer_class = CartProductCountSerializer