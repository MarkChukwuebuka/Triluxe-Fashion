from django.shortcuts import render
from django.views import View

from product.services.product_service import ProductService, ProductReviewService
from services.util import CustomRequestUtil


# Create your views here.
class RetrieveUpdateDeleteProductView(View, CustomRequestUtil):
    template_name = "product-detail.html"
    context_object_name = 'product'
    template_on_error = "product-detail.html#tab-reviews"

    def get(self, request, *args, **kwargs):
        product_service = ProductService(self.request)
        product, error = product_service.fetch_single(kwargs.get("product_id"))

        self.extra_context_data = {
            "title": product.name
        }
        print(product.discounted_price)
        return self.process_request(
            request, target_function=product_service.fetch_single, product_id=kwargs.get("product_id")
        )

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        print("rating")
        product_service = ProductService(self.request)
        product, error = product_service.fetch_single(product_id)

        self.extra_context_data = {
            "title": product.name
        }

        payload = {
            "rating": rating,
            "review": review,
            "product_id": product_id,
        }

        product_review_service = ProductReviewService(self.request)

        return self.process_request(
            request, target_function=product_review_service.create_single,
            target_view="product-detail", payload=payload
        )


class CreateListProductView(View, CustomRequestUtil):
    extra_context_data = {
        "title": "Shop"
    }

    def get(self, request, *args, **kwargs):
        self.template_name = "shop.html"
        self.context_object_name = 'products'

        product_service = ProductService(self.request)

        return self.process_request(
            request, target_function=product_service.fetch_list
        )


class AddOrRemoveFromWishlistView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)


        return JsonResponse({'message': message})