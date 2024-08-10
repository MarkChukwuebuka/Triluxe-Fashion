from django.shortcuts import render
from django.views import View

from product.services.product_service import ProductService
from services.util import CustomRequestUtil


# Create your views here.
class RetrieveUpdateDeleteProductView(View, CustomRequestUtil):

    def get(self, request, *args, **kwargs):
        product_service = ProductService(self.request)

        return self.process_request(
            request, product_service.fetch_single, product_id=kwargs.get("product_id")
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
