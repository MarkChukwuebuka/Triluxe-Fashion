from django.urls import path
from .views import CheckoutView, ShippingDetailView

urlpatterns = [

    path('order-summary/', ShippingDetailView.as_view(), name='shipping-details'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),

]