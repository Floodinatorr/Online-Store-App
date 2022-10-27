from django.shortcuts import render, get_object_or_404
from .models import Store

def StoreDetail(request, slug):
    store = get_object_or_404(Store, slug=slug)
    return render(request, 'store/store_detail.html', context={'store': store})