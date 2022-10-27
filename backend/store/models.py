from django.db import models
from account.models import User

class Store(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='store/images', default='')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='store_members', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self):
        return self.name

class StoreComment(models.Model):
    comment = models.CharField(max_length=1000)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='store_comment_likes')

    class Meta:
        verbose_name = 'Store Comment'
        verbose_name_plural = 'Store Comments'

    def __str__(self):
        return self.comment