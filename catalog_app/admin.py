from django.contrib import admin

from catalog_app.models import Town, Client, Product, Retailer


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ("town_name",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name", "town")
    search_fields = ["first_name", "last_name"]
    filter_vertical = ["product"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name",)


@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "town")
