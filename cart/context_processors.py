from cart.services.cart_service import CartService


def cart(request):
    # Return The default data from our Cart
    return {'cart': CartService(request)}
