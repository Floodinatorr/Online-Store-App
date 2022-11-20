from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('store', StoreViewSet, basename='store')
router.register('store_comment', StoreCommentViewSet, basename='store_comment')

urlpatterns = [
    # path('<slug:slug>/', StoreDetail, name='store_detail'),
    path('', include(router.urls)),
]