from django.contrib import admin
from parler.admin import TranslatableAdmin

from myshop.shop.models import Category, Product
from myshop.exp_to_csv import export_to_csv


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']
    # prepopulated_fields = {'slug': ('name',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

export_to_csv.short_description = 'Export to CSV'


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    # prepopulated_fields = {'slug': ('name',)}
    actions = [export_to_csv]
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
