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
    context_object_name = "products"

    def get(self, request, *args, **kwargs):
        cart_service = CartService(request)

        self.extra_context_data = {
            "title": "Cart",
            'quantities': cart_service.get_quants,
            'totals': cart_service.cart_total(),
        }

        return self.process_request(
            request, target_function=cart_service.get_prods
        )


def cart_add(request):
    # Get the cart
    cart = CartService(request)

    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product_service = ProductService(request)
        product, error = product_service.fetch_single(product_id)
        if error:
            return None, error

        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, "Product Added To Cart..")
        return response


def cart_delete(request):
    cart = CartService(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)

        response = JsonResponse({'product': product_id})

        messages.success(request, "Item Deleted From Shopping Cart")
        return response


def cart_update(request):
    cart = CartService(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty': product_qty})

        messages.success(request, "Your Cart Has Been Updated...")
        return response
