from django.db import models
from account.models import User
from products.models import Product

class CartList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='products_in_cart', blank=True)

    class Meta:
        db_table = 'cart'
        verbose_name_plural = 'Carts'
        verbose_name = 'Cart'

    def __str__(self):
        return self.user.username


class CartProductCount(models.Model):
    cart = models.ForeignKey(CartList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'cart_product_count'
        verbose_name_plural = 'Cart Product Counts'
        verbose_name = 'Cart Product Count'
