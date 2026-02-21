from django.db import models
from django.conf import settings
from store.models import Product


STATUS_CHOICES = [
    ('pending',   'Pending'),
    ('confirmed', 'Confirmed'),
    ('shipped',   'Shipped'),
    ('delivered', 'Delivered'),
]


class Order(models.Model):
    """
    One order per checkout session.
    Linked to the logged-in user.
    total_price is calculated and saved at checkout — not live.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} — {self.status}"


class OrderItem(models.Model):
    """
    A snapshot of each product at the time of purchase.
    price is copied from Product.price at checkout (NOT a live FK).
    This ensures price history is preserved even if product price changes.
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name='order_items'
    )
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # price at time of order

    def __str__(self):
        return f"{self.quantity} × {self.product.name if self.product else 'Deleted Product'}"

    def get_subtotal(self):
        return self.price * self.quantity


class ShippingAddress(models.Model):
    """
    Delivery address saved at checkout.
    OneToOne with Order — every order has exactly one shipping address.
    """
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='shipping_address'
    )
    full_name = models.CharField(max_length=100)
    phone     = models.CharField(max_length=20)
    address   = models.TextField()
    city      = models.CharField(max_length=100)
    country   = models.CharField(max_length=100)
    zip_code  = models.CharField(max_length=20)

    def __str__(self):
        return f"Shipping for Order #{self.order.id} — {self.full_name}"
