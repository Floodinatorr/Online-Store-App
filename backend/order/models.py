from django.db import models
from account.models import User
from store.models import Store
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    card_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    card_cvv = models.CharField(max_length=100)
    card_exp = models.CharField(max_length=100)
    total_price = models.FloatField()
    cancel = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.id