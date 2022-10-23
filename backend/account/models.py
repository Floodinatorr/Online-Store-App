from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=False, null=False, default='avatars/avatar.png')
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    card_name = models.CharField(max_length=100, default='')
    card_number = models.CharField(max_length=100, default='')
    card_cvv = models.CharField(max_length=100, default='')
    card_exp = models.CharField(max_length=100, default='')
    balance = models.FloatField(default=0.0)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

