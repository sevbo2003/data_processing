from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.get_fields()]
    search_fields = ['name', 'atc_code']


admin.site.register(Product, ProductAdmin)
