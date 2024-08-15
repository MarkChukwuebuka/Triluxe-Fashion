from django.db.models import Count, Case, When, ExpressionWrapper, DecimalField, F, Q

from product.models import Product, ProductReview
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
            ),
            reviews_count=Count('reviews')
        )

        return qs

    def fetch_single(self, product_id):
        product = self.__get_base_query().filter(id=product_id).first()
        if not product:
            return None, self.make_error("Product does not exist")

        return product, None


class ProductReviewService(CustomRequestUtil):

    def create_single(self, payload):
        rating = payload.get("rating")
        review = payload.get("review")
        product = payload.get("product")

        product_review, is_created = ProductReview.available_objects.update_or_create(
            user=self.auth_user,
            product=product,
            default=dict(
                rating=rating,
                review=review,
            )
        )

        if not is_created:
            return None, self.make_error("You've already reviewed this product")

        message = "You've successfully reviewed this product"

        return message, None

    def fetch_list(self, product_id):
        q = Q(product_id=product_id)

        return ProductReview.available_objects.filter(q).values(
            "review", "rating", "updated_at",
            first_name=F("user__first_name"),
            last_name=F("user__last_name")
        ).order_by('-created_at')
