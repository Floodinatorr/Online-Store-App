from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=False, null=False, default='avatars/avatar.png')
    phone = models.CharField(max_length=20, blank=False, null=False)
