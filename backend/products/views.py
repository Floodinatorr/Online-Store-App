"""from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

def ProductDetail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request,'product/product_detail.html',context)
"""

from rest_framework import viewsets
from .serializers import *
from .models import *

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductQuestionViewSet(viewsets.ModelViewSet):
    queryset = ProductQuestion.objects.all()
    serializer_class = ProductQuestionSerializer

class ProductQuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = ProductQuestionAnswer.objects.all()
    serializer_class = ProductQuestionAnswerSerializer

class ProductCommentViewSet(viewsets.ModelViewSet):
    queryset = ProductComment.objects.all()
    serializer_class = ProductCommentSerializer

class ProductCommentAnswerViewSet(viewsets.ModelViewSet):
    queryset = ProductCommentAnswer.objects.all()
    serializer_class = ProductCommentAnswerSerializer
