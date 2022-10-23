from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductComment)
admin.site.register(ProductCommentAnswer)
admin.site.register(ProductQuestion)
admin.site.register(ProductQuestionAnswer)

