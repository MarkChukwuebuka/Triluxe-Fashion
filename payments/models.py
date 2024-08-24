from django.db import models
from django.db.models.signals import post_save

from account.models import User
from crm.models import BaseModel
from product.models import Product
import secrets
from payments.paystack import Paystack


class StatusChoices(models.TextChoices):
    ordered = 'Ordered'
    shipped = 'Shipped'
    delivered = 'Delivered'


class Order(BaseModel):

    user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, default="")
    last_name = models.CharField(max_length=250, default="")
    address = models.CharField(max_length=250, default="")
    email = models.EmailField(max_length=250, default="")
    state = models.CharField(max_length=250, default="")
    lga = models.CharField(max_length=250, default="")
    phone = models.CharField(max_length=250, default="")
    paid = models.BooleanField(default=False)
    total_cost = models.IntegerField(default=0)
    status = models.CharField(max_length=25, choices=StatusChoices.choices, default=StatusChoices.ordered)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.user}'


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.order} - {self.product}'



class Payment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.amount}"

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    def amount_value(self):
        return int(self.amount) * 100

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
                self.save()
        if self.verified:
            return True
        else:
            return False