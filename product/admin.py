from django.contrib import admin

from crm.admin import BaseAdmin
from product.models import Tag, Category, Product


# Register your models here.
@admin.register(Tag)
class TagAdmin(BaseAdmin):
    list_display = ["id", "name"] + BaseAdmin.list_display
    search_fields = ["name"]


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    list_display = ["id", "name"] + BaseAdmin.list_display
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    list_display = ["name", "id", "price", "availability"
                    ] + BaseAdmin.list_display
    search_fields = ["name", "description"]
    list_filter = ["rating", "price"]
