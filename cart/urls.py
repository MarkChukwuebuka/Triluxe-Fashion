from django.urls import path
from . import views
from .views import CartView, CheckoutView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),

]
