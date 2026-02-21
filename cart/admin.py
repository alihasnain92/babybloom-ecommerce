from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    """Show cart items inline inside the Cart detail view."""
    model   = CartItem
    extra   = 0
    readonly_fields = ['product', 'quantity']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display  = ['id', 'user', 'created_at']
    search_fields = ['user__username', 'user__email']
    ordering      = ['-created_at']
    inlines       = [CartItemInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display  = ['id', 'cart', 'product', 'quantity']
    search_fields = ['cart__user__username', 'product__name']
