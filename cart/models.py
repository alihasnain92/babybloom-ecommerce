from django.db import models
from django.conf import settings
from store.models import Product


class Cart(models.Model):
    """
    One cart per user (OneToOne).
    Created automatically on first add-to-cart via get_or_create().
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

    def get_total(self):
        """Calculate total price of all items in this cart."""
        return sum(item.get_subtotal() for item in self.cartitem_set.all())


class CartItem(models.Model):
    """
    A product line inside a Cart.
    Quantity can be updated by the user.
    """
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='cartitem_set'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_items'
    )
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"

    def get_subtotal(self):
        """Subtotal for this line item."""
        return self.product.price * self.quantity
