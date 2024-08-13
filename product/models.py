from cloudinary.models import CloudinaryField
from django.db import models

from account.models import User
from crm.models import BaseModel


class Availability(models.TextChoices):
    in_stock = "In Stock"
    out_of_stock = "Out of Stock"


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    percentage_discount = models.IntegerField(null=True, blank=True)
    sku = models.CharField(max_length=255, null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True, related_name="product_tags")
    tags = models.ManyToManyField(Tag, blank=True, related_name="product_categories")
    description = models.TextField(null=True, blank=True)
    availability = models.CharField(max_length=255, choices=Availability.choices, db_default=Availability.in_stock)
    rating = models.IntegerField(null=True, blank=True)

    cover_image = CloudinaryField('cover image', blank=True, null=True)
    image1 = CloudinaryField('image1', blank=True, null=True)
    image2 = CloudinaryField('image2', blank=True, null=True)
    image3 = CloudinaryField('image3', blank=True, null=True)
    image4 = CloudinaryField('image4', blank=True, null=True)
    image5 = CloudinaryField('image5', blank=True, null=True)
    image6 = CloudinaryField('image6', blank=True, null=True)

    def __str__(self):
        return self.name


class ProductReview(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.user__first_name}'s Review on {self.product}"


class UserWishlist(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user__first_name}'s Review on {self.product}"
