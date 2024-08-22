from django.utils import timezone

from payments.models import Order
from services.util import CustomRequestUtil


class OrderService(CustomRequestUtil):

    def create_single(self, payload):
        order, is_created = Order.available_objects.get_or_create(
            user=self.auth_user,
            date_ordered=timezone.now(),
            amount_paid=payload.get("amount_paid"),
            full_name=payload.get("full_name"),
            defaults=dict(
                shipping_address=payload.get("shipping_address"),
                date_shipped=payload.get("date_shipped"),
            )

        )

        if not is_created:
            return None, self.make_error("This order has already been created")

        return order, None

    def fetch_list(self):
        return self.get_base_query()

    def get_base_query(self):
        qs = Order.available_objects

        return qs

    def fetch_single(self, order_id):
        order = self.get_base_query().filter(id=order_id).first()
        if not order:
            return None, self.make_error("Order does not exist")

        return order, None