from django.urls import path
from .views import *

urlpatterns = [
    path('add/<int:id>/<int:count>/', CartAdd, name='cart_add'),
]