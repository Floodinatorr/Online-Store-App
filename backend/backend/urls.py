from django.contrib import admin
from django.urls import path, include
from order.views import AnaSayfa
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', AnaSayfa, name="anasayfa"),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('products/',include('products.urls')),
    path('orders/',include('order.urls')),
    path('stores/',include('store.urls')),
    path('cart/',include('cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
