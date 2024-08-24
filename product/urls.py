from django.urls import path

from product.views import RetrieveUpdateDeleteProductView, CreateListProductView, AddOrRemoveFromWishlistView

urlpatterns = [
    path('<int:product_id>/', RetrieveUpdateDeleteProductView.as_view(), name="product-detail"),
    path('shop/', CreateListProductView.as_view(), name="shop"),

    path('wishlist/add-or-remove/', AddOrRemoveFromWishlistView.as_view(), name='add-remove-from-wishlist'),

]
