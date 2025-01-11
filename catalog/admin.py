from django.contrib import admin
from .models import Product, Categories, Lead


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "purchase_price",
        "category_id",
    )
    list_filter = ("category_id",)
    search_fields = (
        "description",
        "name",
    )


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("description", "name")


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    list_filter = ("created_at", "checkbox")
    search_fields = ("name", "email", "phone")
