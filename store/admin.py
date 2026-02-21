from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['id', 'category_image', 'name', 'created_at']
    search_fields = ['name']
    ordering      = ['name']
    readonly_fields = ['image_preview']

    def category_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:48px;height:48px;object-fit:cover;border-radius:6px;">',
                obj.image.url
            )
        return '—'
    category_image.short_description = 'Image'

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:200px;max-height:200px;'
                'object-fit:cover;border-radius:8px;border:1px solid #eee;">',
                obj.image.url
            )
        return 'No image uploaded yet.'
    image_preview.short_description = 'Current Image'

    # Show live preview above the upload field
    fields = ['name', 'image_preview', 'image']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display   = ['product_image', 'name', 'category', 'price', 'stock_quantity', 'in_stock', 'created_at']
    list_filter    = ['category']
    search_fields  = ['name', 'description']
    list_editable  = ['price', 'stock_quantity']
    ordering       = ['-created_at']
    list_per_page  = 20
    readonly_fields = ['image_preview', 'in_stock']

    # Control field order in the edit form
    fieldsets = (
        ('Product Info', {
            'fields': ('category', 'name', 'description')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'stock_quantity')
        }),
        ('Product Image', {
            'description': '✅ Upload a clear product photo. Recommended: square image, min 400×400px.',
            'fields': ('image_preview', 'image'),   # Preview appears above upload widget
        }),
    )

    # ── Thumbnail in list view ──────────────────────────
    def product_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px;height:60px;'
                'object-fit:cover;border-radius:8px;border:1px solid #eee;">',
                obj.image.url
            )
        return format_html(
            '<span style="color:#ccc;font-size:1.5rem;">📷</span>'
        )
    product_image.short_description = 'Photo'

    # ── Large preview inside the edit form ─────────────
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:300px;max-height:300px;'
                'object-fit:cover;border-radius:10px;border:2px solid #e91e8c;padding:4px;">'
                '<br><small style="color:#888;">✏️ Upload a new image below to replace this one. '
                'Check "Clear" to delete it.</small>',
                obj.image.url
            )
        return format_html(
            '<div style="width:200px;height:150px;background:#fdf8f6;border:2px dashed #e91e8c;'
            'border-radius:10px;display:flex;align-items:center;justify-content:center;color:#e91e8c;">'
            '📷 No image yet<br>Upload one below</div>'
        )
    image_preview.short_description = 'Current Photo'

    # ── Stock badge in list view ───────────────────────
    def in_stock(self, obj):
        if obj.stock_quantity > 10:
            color, label = 'green', f'✅ {obj.stock_quantity}'
        elif obj.stock_quantity > 0:
            color, label = 'orange', f'⚠️ {obj.stock_quantity}'
        else:
            color, label = 'red', '❌ Out'
        return format_html('<span style="color:{};">{}</span>', color, label)
    in_stock.short_description = 'Stock'
