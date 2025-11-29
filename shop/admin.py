from django.contrib import admin
from .models import Products, Bundles

# Register your models here.
admin.site.register(Products)
admin.site.register(Bundles)

# @admin.register(Products)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ("name", "price", "stock", "owner")
#
# @admin.register(Bundles)
# class BundleAdmin(admin.ModelAdmin):
#     list_display = ("name", "price", "stock", "owner")
