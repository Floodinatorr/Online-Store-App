from django.shortcuts import render, get_object_or_404
from .models import Store
from products.models import Product
from order.models import Order

def StoreDetail(request, slug):
    store = get_object_or_404(Store, slug=slug)
    products = Product.objects.filter(store=store)
    product_count = products.count()
    # order_count = Order.objects.filter(store=store).count()
    order_count = 0
    for x in Order.objects.all():
        if x.products.all().filter(store=store):
            order_count += 1
    context = {
        'store': store,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'store/store_detail.html', context)