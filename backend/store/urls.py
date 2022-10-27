from django.urls import path
from .views import StoreDetail

urlpatterns = [
    path('<slug:slug>/', StoreDetail, name='store_detail'),
]