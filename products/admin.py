from django.contrib import admin
from .models import Product, Category, ProductSize


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'has_sizes',
        'available_sizes',
        'size',
        'image'
    )

    ordering = ('sku',)
    inlines = [ProductSizeInline]


class CategoryAdmin(admin.ModelAdmin,):
    list_display = (
        'friendly_name',
        'name'
    )


class ProductSizeAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'label',
        'sku',
        'price',
        'stock',
    )
    list_filter = ('product',)
    search_fields = ('product__name', 'label', 'sku')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductSize, ProductSizeAdmin)
