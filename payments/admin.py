from django.contrib import admin

from crm.admin import BaseAdmin
from payments.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(BaseAdmin):
    list_display = [
        "user", "email", "total_cost", "paid", "status"
    ]
    search_fields = ["address", "email", "state", "first_name"]
    list_filter = ["status", "paid"]



@admin.register(OrderItem)
class OrderItemAdmin(BaseAdmin):
    list_display = [
        "order", "product", "quantity", "price"
    ]
    search_fields = ["price",]
    list_filter = ["product"]

