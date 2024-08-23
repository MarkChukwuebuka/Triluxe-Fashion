from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from cart.services.cart_service import CartService
from payments.services.shipping_address_service import ShippingAddressService
from services.util import CustomRequestUtil


class CheckoutView(View, CustomRequestUtil):
    template_name = "checkout.html"
    context_object_name = "cart_items"

    def get(self, request, *args, **kwargs):
        cart_service = CartService(request)

        self.extra_context_data = {
            "title": "Checkout",
            'totals': cart_service.cart_total(),
            'paystack_key': settings.PAYSTACK_KEY
        }

        return self.process_request(
            request, target_function=cart_service.get_cart_items_with_totals
        )

class ShippingDetailView(LoginRequiredMixin, View, CustomRequestUtil):
    template_name = "shipping-details.html"
    context_object_name = "shipping_detail"

    def get(self, request, *args, **kwargs):
        shipping_service = ShippingAddressService(request)

        self.extra_context_data = {
            "title": "Billing/Shipping Details",
            'totals': CartService(request).cart_total(),
            'cart_items': CartService(request).get_cart_items_with_totals(),
        }

        return self.process_request(
            request, target_function=shipping_service.fetch_single
        )


    def post(self, request, *args, **kwargs):
        shipping_details_service = ShippingAddressService(self.request)
        self.template_on_error = 'shipping-details.html'
        self.template_name = None

        payload = {
            'email': request.POST.get('email'),
            'state': request.POST.get('state'),
            'address': request.POST.get('address'),
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'country': request.POST.get('country'),
            'zipcode': request.POST.get('zipcode'),
            'phone': request.POST.get('phone'),
            'city': request.POST.get('city'),
        }

        self.extra_context_data = {
            "title": "Billing/Shipping Details",
            'totals': CartService(request).cart_total(),
            'cart_items': CartService(request).get_cart_items_with_totals(),
        }

        return self.process_request(
            request, target_view="checkout", target_function=shipping_details_service.create_single, payload=payload
        )

