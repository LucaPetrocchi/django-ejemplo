from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from products.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ("name", "price")
    search_fields = ("price", "category", "desc", "name")
    list_filter = ("category", "name")
    list_editable = ("category", "price", "stock", "desc")
    list_display = [
        "name",
        "category",
        "price",
        "stock",
        "desc",
        "get_price_range",
        "get_total",
        "get_stock",
    ]

    fieldsets = [
        (
            "product info",
            {
                "fields": [
                    "name",
                    "price",
                    "desc",
                ]
            },
        ),
        (
            "more info",
            {
                "classes": ['collapse'],
                "fields": ['stock',],
            }
        )
    ]

    def get_total(self, obj):
        return obj.price * obj.stock

    def get_stock(self, obj):
        poco = "#ff0000"
        mucho = "#008000"
        normal = "#ffd300"
        if obj.stock < 100:
            codigo = poco
        elif obj.stock > 300:
            codigo = mucho
        else:
            codigo = normal

        return format_html('<span style="color: {}"> {} </span>', codigo, obj.stock)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]