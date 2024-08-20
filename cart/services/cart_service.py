from account.models import Profile
from product.models import Product
from product.services.product_service import ProductService
from services.util import CustomRequestUtil


class CartService(CustomRequestUtil):

    def add(self, product, quantity):

        product_id = str(product)
        product_qty = str(quantity)

        if product_id in self.cart:
            error = "This item is already in your cart"
            return None, error
        else:
            self.cart[product_id] = int(product_qty)
            message = "This item has been added to your cart successfully"

        self.session.modified = True

        # if self.auth_user:
        #     current_user = self.auth_profile
        #     # Convert {'3':1, '2':4} to {"3":1, "2":4}
        #     old_cart = str(self.cart)
        #     old_cart = old_cart.replace("\'", "\"")
        #     current_user.update(old_cart=str(old_cart))

        return message, None

    def cart_total(self):
        product_ids = self.cart.keys()

        product_service = ProductService(self.request)
        products = product_service.get_base_query().filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.percentage_discount:
                        total = total + (product.discounted_price * value)
                    else:
                        total = total + (product.price * value)
        return total

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        product_ids = self.cart.keys()

        product_service = ProductService(self.request)
        products = product_service.get_base_query().filter(id__in=product_ids)

        return products

    def get_cart_items_with_totals(self):
        """
        Returns a list of products in the cart with their associated quantities and totals.
        """
        product_ids = self.cart.keys()
        product_service = ProductService(self.request)
        products = product_service.get_base_query().filter(id__in=product_ids)

        cart_quants_totals = []
        for product in products:
            product_id_str = str(product.id)
            quantity = self.cart[product_id_str]
            if product.percentage_discount:
                total = product.discounted_price * quantity
            else:
                total = product.price * quantity

            cart_quants_totals.append({
                'product': product,
                'quantity': quantity,
                'total': total,
            })

        return cart_quants_totals

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):

        product_id = str(product)
        product_qty = int(quantity)

        cart = self.cart
        cart[product_id] = product_qty

        self.session.modified = True
        message = "you've successfully update your cart"

        if self.auth_user:
            current_user = self.auth_profile
            # Convert {'3':1, '2':4} to {"3":1, "2":4}
            old_cart = str(self.cart)
            old_cart = old_cart.replace("\'", "\"")
            # Save old_cart to the Profile Model
            current_user.update(old_cart=str(old_cart))

        return message, None

    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
        message = "Item was successfully removed from cart"

        if self.request.user.is_authenticated:
            # Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert {'3':1, '2':4} to {"3":1, "2":4}
            old_cart = str(self.cart)
            old_cart = old_cart.replace("\'", "\"")
            # Save old_cart to the Profile Model
            current_user.update(old_cart=str(old_cart))

        return message, None

