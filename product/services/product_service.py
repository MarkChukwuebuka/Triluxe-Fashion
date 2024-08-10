from django.db.models import Count, Case, When, ExpressionWrapper, DecimalField, F

from product.models import Product
from services.util import CustomRequestUtil


class ProductService(CustomRequestUtil):

    def create_single(self, payload):
        pass

    def fetch_list(self):
        return self.__get_base_query()

    def __get_base_query(self):
        qs = Product.available_objects.prefetch_related(
            "categories", "tags"
        ).order_by("rating", "-updated_at")

        qs = qs.annotate(
            discounted_price=Case(
                When(percentage_discount__gt=0, then=ExpressionWrapper(
                    F('price') * (1 - F('percentage_discount') / 100),
                    output_field=DecimalField(max_digits=15, decimal_places=2)
                )),
                default=F('price'),
                output_field=DecimalField(max_digits=15, decimal_places=2)
            )
        )

        return qs

    def fetch_single(self, product_id):
        product = self.__get_base_query().filter(id=product_id).first()
        if not product:
            return None, self.make_error("Product does not exist")

        return product, None
