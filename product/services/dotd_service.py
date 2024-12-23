from django.db.models import Q, F, DecimalField, ExpressionWrapper, When, Case
from django.utils import timezone

from product.models import DealOfTheDay, TopShopper
from services.util import CustomRequestUtil




class DOTDService(CustomRequestUtil):

    def fetch_active_deals(self):
        q = Q(is_active=True)

        return self.get_base_query().filter(q)


    def get_base_query(self):
        qs = DealOfTheDay.available_objects.select_related("product")

        qs = qs.annotate(
            discounted_price=Case(
                When(
                    product__percentage_discount__isnull=False,
                    product__percentage_discount__gt=0,
                    then=ExpressionWrapper(
                        F('product__price') - (F('product__price') * F('product__percentage_discount') / 100),
                        output_field=DecimalField(max_digits=15, decimal_places=2),
                    )
                ),
                default=F('product__price'),
                output_field=DecimalField(max_digits=15, decimal_places=2),
            )
        )

        return qs

    def toggle_active_state(self):

        now = timezone.now()
        for deal in DealOfTheDay.available_objects:
            deal.is_active = True if deal.start_time <= now <= deal.end_time else False
            deal.save()

        return None


class TopShopperService(CustomRequestUtil):

    def fetch_list(self):
        return self.get_base_query()[:3]


    def get_base_query(self):
        return TopShopper.available_objects.order_by('-id')
