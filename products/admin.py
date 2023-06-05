from django.contrib import admin

from products.models import ProductCategory, Product, Basket


admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ['image', 'name', 'description', ('price', 'quantity'), 'category']
    search_fields = ['name']
    ordering = ['name']

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity', 'timestamp']
    readonly_fields = ['timestamp']
    extra = 0

