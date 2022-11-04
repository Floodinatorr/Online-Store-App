from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:slug>/', ProductDetail, name='product_detail'),
]