from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('order', OrderViewSet, basename='order')

urlpatterns = [
    # path('<slug:slug>/', StoreDetail, name='store_detail'),
    path('', include(router.urls)),
]