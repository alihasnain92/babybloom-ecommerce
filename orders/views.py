from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart, CartItem
from .models import Order, OrderItem, ShippingAddress
from .forms import CheckoutForm


@login_required
def checkout_view(request):
    """
    GET  /checkout/ → Show shipping form + order summary from cart.
    POST /checkout/ → Validate form → Create Order → Create OrderItems
                      (with price snapshot) → Create ShippingAddress
                      → Clear cart → Redirect to confirmation page.
    """
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.select_related('product').all()

    if not cart_items.exists():
        messages.warning(request, 'Your cart is empty. Add some items first!')
        return redirect('shop')

    # Calculate total from live cart
    total = cart.get_total()

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # 1. Create the Order (price snapshot at checkout time)
            order = Order.objects.create(
                user=request.user,
                total_price=total,
                status='pending',
            )

            # 2. Create OrderItems — save price at time of purchase
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,  # ← price snapshot ✅
                )
                # Reduce stock
                item.product.stock_quantity -= item.quantity
                item.product.save()

            # 3. Save shipping address linked to this order
            shipping = form.save(commit=False)
            shipping.order = order
            shipping.save()

            # 4. Clear the cart
            cart_items.delete()

            messages.success(request, f'Order #{order.id} placed successfully! 🎉')
            return redirect('order_confirm', order_id=order.id)
        else:
            messages.error(request, 'Please fix the errors in the shipping form.')
    else:
        form = CheckoutForm()

    return render(request, 'orders/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'total': total,
    })


@login_required
def order_confirm(request, order_id):
    """
    GET /order/confirmation/<order_id>/ → Thank you / success page.
    Only the order owner can view this page.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.items.select_related('product').all()
    shipping = get_object_or_404(ShippingAddress, order=order)

    return render(request, 'orders/order_confirm.html', {
        'order': order,
        'order_items': order_items,
        'shipping': shipping,
    })


@login_required
def order_history(request):
    """
    GET /orders/ → List all orders for the logged-in user (newest first).
    """
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'orders/order_history.html', {
        'orders': orders,
    })


@login_required
def order_detail(request, order_id):
    """
    GET /orders/<order_id>/ → Full detail of a single order.
    Only the order owner can access this.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.items.select_related('product').all()
    shipping = ShippingAddress.objects.filter(order=order).first()

    return render(request, 'orders/order_detail.html', {
        'order': order,
        'order_items': order_items,
        'shipping': shipping,
    })
