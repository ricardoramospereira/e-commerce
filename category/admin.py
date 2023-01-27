from django.contrib import admin
from .models import Category
from django.utils.html import format_html

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('category_name',)}
   list_display = ("category_name", "slug",)
