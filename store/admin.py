from django.contrib import admin
from .models import Category, Product, Order, ProductSize

admin.site.register(Category)
admin.site.register(Product)
admin.site.register( Order)
admin.site.register(ProductSize)


