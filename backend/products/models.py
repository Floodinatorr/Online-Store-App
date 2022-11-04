from django.db import models
from account.models import User
from store.models import Store
from django.core.validators import MaxValueValidator
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    discount = models.IntegerField()
    image = models.ImageField(upload_to='product/images', default='')
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def give_discount_price(self):
        new = self.price - (self.price * self.discount / 100)
        asd = "{:.2f}".format(new)
        return asd

    def __str__(self):
        return self.name

class ProductQuestion(models.Model):
    question = models.CharField(max_length=1000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='product_question_likes')

    class Meta:
        verbose_name = 'Product Question'
        verbose_name_plural = 'Product Questions'

    def __str__(self):
        return self.question

class ProductQuestionAnswer(models.Model):
    answer = models.CharField(max_length=1000)
    question = models.ForeignKey(ProductQuestion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='product_question_answers_likes')

    class Meta:
        verbose_name = 'Product Question Answer'
        verbose_name_plural = 'Product Question Answers'

    def __str__(self):
        return self.answer        

class ProductComment(models.Model):
    comment = models.CharField(max_length=1000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='product_comment_likes')

    class Meta:
        verbose_name = 'Product Comment'
        verbose_name_plural = 'Product Comments'

    def __str__(self):
        return self.comment

class ProductCommentAnswer(models.Model):
    answer = models.CharField(max_length=1000)
    comment = models.ForeignKey(ProductComment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='product_comment_answers_likes')

    class Meta:
        verbose_name = 'Product Comment Answer'
        verbose_name_plural = 'Product Comment Answers'

    def __str__(self):
        return self.answer