from django.urls import path, include
from . import views
from .views import CartView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/', views.cart_add, name='cart_add'),
    path('delete/', views.cart_delete, name='cart_delete'),
    path('update/', views.cart_update, name='cart_update'),
]