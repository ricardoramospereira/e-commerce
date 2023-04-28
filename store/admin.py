from django.contrib import admin
from .models import Product, Variation

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modifield_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    list_editable = ('is_available',)

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variations_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variations_category', 'variation_value')
