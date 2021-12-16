from django.contrib import admin
from .models import Product, Category, Brand, Comment, Cart
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Product, MarkdownxModelAdmin)
admin.site.register(Comment)
admin.site.register(Cart)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Brand, BrandAdmin)