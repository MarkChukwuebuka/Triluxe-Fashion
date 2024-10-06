from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from product.services.product_service import ProductService, ProductReviewService, WishlistService
from services.util import CustomRequestUtil


# Create your views here.
class RetrieveUpdateDeleteProductView(View, CustomRequestUtil):
    template_name = "product-detail.html"
    context_object_name = 'product'
    template_on_error = "product-detail.html"

    def get(self, request, *args, **kwargs):
        product_service = ProductService(self.request)
        product, error = product_service.fetch_single(kwargs.get("product_id"))

        self.extra_context_data = {
            "title": product.name
        }

        return self.process_request(
            request, target_function=product_service.fetch_single, product_id=kwargs.get("product_id")
        )

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        rating = request.POST.get('rating')
        review = request.POST.get('review')

        product_service = ProductService(self.request)
        product, error = product_service.fetch_single(product_id)

        self.extra_context_data = {
            "title": product.name,
            'product':product
        }

        payload = {
            "rating": rating,
            "review": review,
            "product": product,
        }

        product_review_service = ProductReviewService(self.request)

        return self.process_request(
            request, target_function=product_review_service.create_single,
            target_view="product-detail", payload=payload
        )


class CreateListProductView(View, CustomRequestUtil):
    extra_context_data = {
        "title": "Luxe Shop"
    }

    def get(self, request, *args, **kwargs):
        self.template_name = "shop.html"
        self.context_object_name = 'products'

        product_service = ProductService(self.request)

        return self.process_request(
            request, target_function=product_service.fetch_list
        )

class AddOrRemoveFromWishlistView(View, CustomRequestUtil):
    def post(self, request, *args, **kwargs):
        product_id = int(request.POST.get('product_id'))
        wishlist_service = WishlistService(self.request)

        message, error = wishlist_service.add_or_remove({"product": product_id})

        if error:
            return JsonResponse({"error": error}, status=400)

        return JsonResponse({"message": message})


class WishlistView(View, CustomRequestUtil):
    extra_context_data = {
        "title":"My Wishlist"
    }
    def get(self, request, *args, **kwargs):
        self.template_name = "wishlist.html"
        self.context_object_name = 'wishlist_items'

        wishlist_service = WishlistService(self.request)

        return self.process_request(
            request, target_function=wishlist_service.fetch_list
        )
