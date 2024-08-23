from cart.services.cart_service import Cart


def cart(request):
    return {'cart': Cart(request)}