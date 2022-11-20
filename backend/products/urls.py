from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')
router.register('product_question', ProductQuestionViewSet, basename='product_question')
router.register('product_question_answer', ProductQuestionAnswerViewSet, basename='product_question_answer')
router.register('product_comment', ProductCommentViewSet, basename='product_comment')
router.register('product_comment_answer', ProductCommentAnswerViewSet, basename='product_comment_answer')

urlpatterns = [
    # path('<slug:slug>/', StoreDetail, name='store_detail'),
    path('', include(router.urls)),
]