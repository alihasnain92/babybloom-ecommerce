from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress


class OrderItemInline(admin.TabularInline):
    """Show order items inline inside the Order detail view."""
    model           = OrderItem
    extra           = 0
    readonly_fields = ['product', 'quantity', 'price']


class ShippingAddressInline(admin.StackedInline):
    """Show shipping address inline inside the Order detail view."""
    model     = ShippingAddress
    extra     = 0
    readonly_fields = [
        'full_name', 'phone', 'address', 'city', 'country', 'zip_code'
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display  = ['id', 'user', 'total_price', 'status', 'created_at']
    list_filter   = ['status']
    search_fields = ['user__username', 'user__email']
    ordering      = ['-created_at']
    list_per_page = 20
    inlines       = [OrderItemInline, ShippingAddressInline]

    # Allow changing order status directly from the list view
    list_editable = ['status']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display  = ['id', 'order', 'product', 'quantity', 'price']
    search_fields = ['product__name', 'order__user__username']


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display  = ['id', 'order', 'full_name', 'city', 'country']
    search_fields = ['full_name', 'city', 'country', 'phone']
