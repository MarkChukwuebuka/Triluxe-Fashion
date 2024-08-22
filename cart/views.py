from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.views import View

from cart.services.cart_service import CartService
from product.models import Product
from product.services.product_service import ProductService
from services.util import CustomRequestUtil


class CartView(View, CustomRequestUtil):
    template_name = "cart.html"
    context_object_name = "cart_items"

    def get(self, request, *args, **kwargs):
        cart_service = CartService(request)

        self.extra_context_data = {
            "title": "Cart",
            'totals': cart_service.cart_total(),
        }

        return self.process_request(
            request, target_function=cart_service.get_cart_items_with_totals
        )

    def post(self, request, *args, **kwargs):
        cart_service = CartService(request)
        action = request.POST.get('action')

        if action == 'add':

            product_id = int(request.POST.get('product_id'))
            quantity = int(request.POST.get('product_qty'))

            return self.process_request(
                request, target_function=cart_service.add, quantity=quantity, product=product_id
            )

        elif action == 'update':

            product_id = int(request.POST.get('product_id'))
            quantity = int(request.POST.get('product_qty'))

            return self.process_request(
                request, target_function=cart_service.update, quantity=quantity, product=product_id
            )

        elif action == 'delete':

            product_id = int(request.POST.get('product_id'))

            return self.process_request(
                request, target_function=cart_service.delete, product=product_id
            )

        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)


