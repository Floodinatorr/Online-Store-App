from django.shortcuts import render, get_object_or_404
from .models import Store
from products.models import Product
from order.models import Order
from django.http import HttpResponse

def StoreDetail(request, slug):
    store = get_object_or_404(Store, slug=slug)
    products = Product.objects.filter(store=store)
    product_count = products.count()
    order = request.GET.get('ORDER')
    if order == 'priceLow':
        products = products.order_by('price')
    elif order == 'priceHigh':
        products = products.order_by('-price')
    elif order == 'mostLiked':
        products = products.order_by('-likes')
    filter_price = request.GET.get('PRICE')

    if filter_price:
        if int(filter_price) <= 0:
            return HttpResponse('Invalid Price')
            
    order_count = 0
    for x in Order.objects.all():
        if x.products.all().filter(store=store):
            order_count += 1
    context = {
        'store': store,
        'product_count': product_count,
        'order_count': order_count,
        'products': products,
    }
    return render(request, 'store/store_detail.html', context)