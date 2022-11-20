from rest_framework import serializers
from .models import *

class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartList
        fields = '__all__'

class CartProductCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProductCount
        fields = '__all__'