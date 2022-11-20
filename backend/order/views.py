"""
from django.shortcuts import render

def AnaSayfa(request):
    return render(request,'index.html',{})
"""

from rest_framework import viewsets
from .serializers import *
from .models import *

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
