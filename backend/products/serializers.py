from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuestion
        fields = '__all__'

class ProductQuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuestionAnswer
        fields = '__all__'

class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = '__all__'

class ProductCommentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCommentAnswer
        fields = '__all__'