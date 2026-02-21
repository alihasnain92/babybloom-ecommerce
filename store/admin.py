from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name', 'created_at']
    search_fields = ['name']
    ordering      = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display   = ['id', 'name', 'category', 'price', 'stock_quantity', 'created_at']
    list_filter    = ['category']
    search_fields  = ['name', 'description']
    list_editable  = ['price', 'stock_quantity']   # Edit price/stock inline in list view
    ordering       = ['-created_at']
    list_per_page  = 20
