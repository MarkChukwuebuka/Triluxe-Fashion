from django.utils import timezone

from crm.models import Subscriber
from payments.models import Order
from services.util import CustomRequestUtil


class NewsLetterService(CustomRequestUtil):

    def create_single(self, payload):
        subscriber, is_created = Subscriber.objects.get_or_create(
            email=payload.get('email')
        )

        if not is_created:
            return None, self.make_error("Email is already subscribed")

        return subscriber, None

