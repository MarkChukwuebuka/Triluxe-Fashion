from django.contrib import admin

from crm.admin import BaseAdmin
from payments.models import ShippingAddress, Order, OrderItem


@admin.register(ShippingAddress)
class ShippingAddressAdmin(BaseAdmin):
    list_display = ["user", "first_name", "last_name", "email", "state"]
    search_fields = ["first_name", "last_name", "email", "state", "address1"]
    list_filter = ["state", "user"]



@admin.register(Order)
class OrderAdmin(BaseAdmin):
    list_display = [
        "user", "email", "shipped", "amount_paid", "date_ordered", "date_shipped"
    ]
    search_fields = ["full_name", "email", "state", "address1"]
    list_filter = ["date_ordered", "shipped", "date_shipped"]



@admin.register(OrderItem)
class OrderItemAdmin(BaseAdmin):
    list_display = [
        "order", "product", "user", "quantity", "price"
    ]
    search_fields = ["price", "user"]
    list_filter = ["user", "product"]

