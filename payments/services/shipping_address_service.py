from django.utils import timezone

from payments.models import ShippingAddress
from services.util import CustomRequestUtil, format_phone_number


class ShippingAddressService(CustomRequestUtil):

    def create_single(self, payload):
        phone = format_phone_number(payload.get("phone"))

        _, _ = ShippingAddress.available_objects.update_or_create(
            user=self.auth_user,
            email=payload.get("email"),
            defaults=dict(
                first_name=payload.get("first_name"),
                last_name=payload.get("last_name"),
                address1=payload.get("address1"),
                address2=payload.get("address2"),
                city=payload.get("city"),
                state=payload.get("state"),
                country=payload.get("country"),
                zipcode=payload.get("zipcode"),
                phone=phone
            )

        )
        message = "Your billing/shipping details were saved successfully"

        return message, None


    def get_base_query(self):
        qs = ShippingAddress.available_objects

        return qs

    def fetch_single(self):
        address = self.get_base_query().filter(user=self.auth_user).first()
        if not address:
            return None, self.make_error("Shipping Address does not exist")

        return address, None