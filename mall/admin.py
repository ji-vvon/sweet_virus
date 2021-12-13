from django.contrib import admin
from .models import Product, Category, Brand


admin.site.register(Product)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Brand, BrandAdmin)