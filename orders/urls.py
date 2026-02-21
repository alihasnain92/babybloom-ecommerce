from django.urls import path
from . import views

urlpatterns = [
    path('checkout/',                             views.checkout_view,  name='checkout'),
    path('order/confirmation/<int:order_id>/',    views.order_confirm,  name='order_confirm'),
    path('orders/',                               views.order_history,  name='order_history'),
    path('orders/<int:order_id>/',                views.order_detail,   name='order_detail'),
]
