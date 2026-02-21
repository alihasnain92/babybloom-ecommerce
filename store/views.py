from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home_view(request):
    """
    GET / → Homepage with featured products (latest 8) and all categories.
    """
    categories = Category.objects.all()
    featured_products = Product.objects.filter(stock_quantity__gt=0).order_by('-created_at')[:8]

    return render(request, 'store/home.html', {
        'categories': categories,
        'featured_products': featured_products,
    })


def shop_view(request):
    """
    GET /shop/ → All products, with optional search query.
    """
    query = request.GET.get('q', '')
    categories = Category.objects.all()
    products = Product.objects.filter(stock_quantity__gt=0)

    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'store/shop.html', {
        'products': products,
        'categories': categories,
        'query': query,
    })


def category_view(request, id):
    """
    GET /shop/category/<id>/ → Products filtered by category.
    """
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category, stock_quantity__gt=0)
    categories = Category.objects.all()

    return render(request, 'store/category.html', {
        'category': category,
        'products': products,
        'categories': categories,
    })


def product_view(request, id):
    """
    GET /shop/product/<id>/ → Single product detail page.
    """
    product = get_object_or_404(Product, id=id)
    related_products = Product.objects.filter(
        category=product.category,
        stock_quantity__gt=0
    ).exclude(id=product.id)[:4]

    return render(request, 'store/product.html', {
        'product': product,
        'related_products': related_products,
    })
