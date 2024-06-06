from django.contrib import admin

from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Product, ProductAdmin)
