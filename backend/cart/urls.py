from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cart_list', CartListViewSet, basename='cart_list')
router.register('cart_product_count', CartProductCountViewSet, basename='cart_product_count')

urlpatterns = [
    # path('<slug:slug>/', StoreDetail, name='store_detail'),
    path('', include(router.urls)),
]