from django.urls import path
from . import views
from payments.views import verify_payment, start_order

urlpatterns = [
    path('order/', start_order, name='start_order'),
    path('verify_payment<str:ref>/', verify_payment, name='verify_payment')

]
