from django.urls import path
from . import views

urlpatterns = [
    path('',                             views.home_view,     name='home'),
    path('shop/',                        views.shop_view,     name='shop'),
    path('shop/category/<int:id>/',      views.category_view, name='category'),
    path('shop/product/<int:id>/',       views.product_view,  name='product'),
]
