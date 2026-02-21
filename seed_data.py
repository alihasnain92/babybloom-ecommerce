"""
BabyBloom — Sample Data Seeder
Run: venv\Scripts\python seed_data.py
Creates 4 categories and 8 products for testing.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'babybloom.settings')
django.setup()

from store.models import Category, Product

# ── Clear old seed data ──────────────────────────────
Product.objects.all().delete()
Category.objects.all().delete()
print("Cleared existing data.")

# ── Create Categories ────────────────────────────────
categories = [
    Category(name="Clothing"),
    Category(name="Feeding & Nursing"),
    Category(name="Skincare"),
    Category(name="Toys & Comfort"),
]
Category.objects.bulk_create(categories)
categories = {c.name: c for c in Category.objects.all()}
print(f"Created {len(categories)} categories.")

# ── Create Products ──────────────────────────────────
products = [
    Product(category=categories["Clothing"],        name="Organic Cotton Onesie",         description="Ultra-soft 100% organic cotton onesie, perfect for newborns. Gentle on sensitive skin.",              price=14.99, stock_quantity=50),
    Product(category=categories["Clothing"],        name="Newborn Sleep Gown",             description="Cozy sleep gown with easy snap closure at the bottom for quick nighttime changes.",                     price=18.50, stock_quantity=35),
    Product(category=categories["Clothing"],        name="Baby Knit Booties Set",          description="Adorable hand-knit booties to keep tiny feet warm. Includes 3 pairs.",                                price=9.99,  stock_quantity=60),
    Product(category=categories["Feeding & Nursing"], name="Silicone Soft-Spout Sippy Cup", description="BPA-free silicone sippy cup with soft spout, easy grip handles, and spill-proof lid.",               price=12.99, stock_quantity=40),
    Product(category=categories["Feeding & Nursing"], name="Bamboo Muslin Bibs (5 Pack)",  description="Super-absorbent bamboo muslin bibs with adjustable snap closure. Hypoallergenic.",                   price=16.99, stock_quantity=55),
    Product(category=categories["Skincare"],        name="Gentle Baby Wash & Shampoo",    description="Tear-free, fragrance-free baby wash and shampoo. Dermatologist tested for newborn skin.",             price=11.49, stock_quantity=45),
    Product(category=categories["Skincare"],        name="Soothing Diaper Rash Cream",    description="Fast-acting zinc oxide cream that soothes and protects baby's delicate skin.",                        price=8.99,  stock_quantity=70),
    Product(category=categories["Toys & Comfort"],  name="Plush Rainbow Rattle Toy",      description="Colorful, BPA-free rattle with soft plush body. Great for developing motor skills in newborns.",      price=13.50, stock_quantity=30),
]
Product.objects.bulk_create(products)
print(f"Created {len(products)} products.")

# ── Summary ──────────────────────────────────────────
print("\n=== Seed Complete ===")
for cat in Category.objects.all():
    count = cat.products.count()
    print(f"  {cat.name}: {count} product(s)")
print(f"\nTotal products: {Product.objects.count()}")
print("Done! Visit http://127.0.0.1:8000/shop/ to see them.")
