from django.urls import path

from product.views import RetrieveUpdateDeleteProductView, CreateListProductView

urlpatterns = [
    path('<int:product_id>/', RetrieveUpdateDeleteProductView.as_view(), name="product-detail"),
    path('', CreateListProductView.as_view(), name="product-create-list"),

]
