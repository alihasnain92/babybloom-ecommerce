"""
BabyBloom — Main URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Store (home, shop, product pages) — mounted at root
    path('', include('store.urls')),

    # Auth (signup, login, logout) — mounted at root
    path('', include('users.urls')),

    # Cart — mounted at /cart/
    path('cart/', include('cart.urls')),

    # Orders (checkout, order history) — mounted at root
    path('', include('orders.urls')),

    # Contact — mounted at root
    path('', include('contact.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
