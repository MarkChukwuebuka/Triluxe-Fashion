from django.views import View

from crm.models import Subscriber
from crm.services.newsletter_service import NewsLetterService
from product.services.dotd_service import DOTDService, TopShopperService
from product.services.product_service import ProductService
from services.util import CustomRequestUtil


# Create your views here.
class HomeView(View, CustomRequestUtil):
    template_name = "index.html"
    extra_context_data = {
        "title": "Welcome",
    }

    def get(self, request, *args, **kwargs):
        product_service = ProductService(self.request)

        products = product_service.fetch_list()[:10]
        deals = DOTDService(self.request).fetch_active_deals()
        top_shoppers = TopShopperService(self.request).fetch_list()

        self.extra_context_data["products"] = products
        self.extra_context_data["deals"] = deals
        self.extra_context_data["top_shoppers"] = top_shoppers

        return self.process_request(request)

    def post(self, request, *args, **kwargs):
        nl_service = NewsLetterService(self.request)
        self.template_name = None
        self.template_on_error = None


        payload = {
            'email': request.POST.get('first_name')
        }

        return self.process_request(
            request, target_view="home", target_function=nl_service.create_single, payload=payload
        )



# def unsubscribe(request, email):
#     try:
#         subscriber = Subscriber.objects.filter(email=email).first()
#         subscriber.is_active = False
#         subscriber.save()
#         messages.success(request, "You have successfully unsubscribed.")
#     except Subscriber.DoesNotExist:
#         messages.error(request, "Email not found.")
#     return redirect('subscribe')


class ContactView(View, CustomRequestUtil):
    template_name = "contact.html"
    extra_context_data = {
        "title": "Contact Us",
    }

    def get(self, request, *args, **kwargs):
        return self.process_request(request)


class AboutView(View, CustomRequestUtil):
    template_name = "about.html"
    extra_context_data = {
        "title": "About Us",
    }

    def get(self, request, *args, **kwargs):
        return self.process_request(request)
