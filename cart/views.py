from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from store.models import Product
from .models import Cart, CartItem


@login_required
def cart_view(request):
    """
    GET /cart/ → Show all cart items and total.
    Cart is created via get_or_create so no cart = empty cart page.
    """
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.select_related('product').all()
    total = cart.get_total()

    return render(request, 'cart/cart.html', {
        'cart': cart,
        'cart_items': cart_items,
        'total': total,
    })


@login_required
def add_to_cart(request, product_id):
    """
    POST /cart/add/<product_id>/ → Add product to cart.
    Creates cart if it doesn't exist.
    If item already in cart → increment quantity.
    """
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)

        if product.stock_quantity < 1:
            messages.error(request, f'Sorry, "{product.name}" is out of stock.')
            return redirect('product', id=product_id)

        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f'"{product.name}" quantity updated in cart.')
        else:
            messages.success(request, f'"{product.name}" added to your cart! 🛒')

    return redirect('cart')


@login_required
def update_cart_item(request, item_id):
    """
    POST /cart/update/<item_id>/ → Update quantity of a cart item.
    If quantity <= 0 → remove item.
    """
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        quantity = int(request.POST.get('quantity', 1))

        if quantity <= 0:
            cart_item.delete()
            messages.info(request, 'Item removed from cart.')
        else:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated.')

    return redirect('cart')


@login_required
def remove_cart_item(request, item_id):
    """
    POST /cart/remove/<item_id>/ → Delete a line item from cart.
    """
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        cart_item.delete()
        messages.info(request, 'Item removed from your cart.')

    return redirect('cart')
