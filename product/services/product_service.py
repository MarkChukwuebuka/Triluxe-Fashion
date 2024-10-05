from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Case, When, ExpressionWrapper, DecimalField, F, Q, Value
from django.db.models.functions import Coalesce
from django.utils import timezone

from product.models import Product, ProductReview, Wishlist, DealOfTheDay
from services.util import CustomRequestUtil


class ProductService(CustomRequestUtil):

    def create_single(self, payload):
        pass

    def fetch_list(self):
        return self.get_base_query()

    def get_base_query(self):
        qs = Product.available_objects.prefetch_related(
            "categories", "tags"
        ).order_by("rating", "-updated_at")

        qs = qs.annotate(
            discounted_price=Case(
                When(
                    percentage_discount__isnull=False,
                    percentage_discount__gt=0,
                    then=ExpressionWrapper(
                        F('price') - ((F('percentage_discount') * F("price")) / 100),
                        output_field=DecimalField(max_digits=15, decimal_places=2)
                    )
                ),
                default=F('price'),
                output_field=DecimalField(max_digits=15, decimal_places=2)
            ),

            reviews_count=Count('reviews')
        )

        return qs

    def fetch_single(self, product_id):
        product = self.get_base_query().filter(id=product_id).first()
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
            defaults=dict(
                rating=rating,
                review=review,
            )
        )

        if not is_created:
            return "You've updated your review on this product", None

        message = "You've successfully reviewed this product"

        return message, None

    def fetch_list(self, product_id):
        q = Q(product_id=product_id)

        return ProductReview.available_objects.filter(q).values(
            "review", "rating", "updated_at",
            first_name=F("user__first_name"),
            last_name=F("user__last_name")
        ).order_by('-created_at')


class WishlistService(CustomRequestUtil, LoginRequiredMixin):

    def add_or_remove(self, payload):
        message = None
        error = None
        product = payload.get("product")

        wishlist_item, is_created = Wishlist.available_objects.get_or_create(
            user=self.auth_user,
            product_id=product,
        )

        if is_created:
            message = "Added to wishlist"
        else:
            self.hard_delete(wishlist_item)
            error = "Removed from wishlist"

        return message, error

    def fetch_list(self):
        q = Q(user=self.auth_user)

        return Wishlist.available_objects.filter(q).values(
            "product_id",
            product_name=F("product__name"), product_availability=F("product__availability"),
            product_price=F("product__price"), product_image=F("product__cover_image")

        ).order_by('-created_at')


    def hard_delete(self, wishlist_item):
        wishlist_item.delete()

        return wishlist_item, None


class DOTDService(CustomRequestUtil):

    def fetch_active_deals(self):
        q = Q(is_active=True)

        return self.get_base_query().filter(q)


    def get_base_query(self):
        return DealOfTheDay.available_objects.select_related("product")

    def toggle_active_state(self):

        now = timezone.now()
        for deal in DealOfTheDay.available_objects:
            deal.is_active = True if deal.start_time <= now <= deal.end_time else False
            deal.save()

        return None
