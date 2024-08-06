from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices, Q

from crm.models import BaseModel


class UserTypes(TextChoices):
    admin = "Admin"
    customer = "Customer"


class User(AbstractUser, BaseModel):
    username = models.CharField(max_length=60, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=70, null=True, blank=True)
    image_url = models.URLField(null=True)
    user_type = models.CharField(
        max_length=255, default=UserTypes.admin, choices=UserTypes.choices
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    date_joined = None

    roles = models.ManyToManyField(
        "Role", related_query_name="roles", blank=True
    )

    groups = None
    user_permissions = None

    def get_short_name(self):
        return self.get_full_name()

    def get_full_name(self):
        return " ".join(
            [
                self.first_name or "",
                self.last_name or "",
                self.other_names or "",
            ]
        ).replace("\s+", " ").strip()

    def has_permission(self, perm_name):
        if self.is_superuser:
            return True

        q = Q(permissions__name=perm_name)

        return self.roles.filter(q).exists()

    def __str__(self):
        return self.get_full_name() + f" ({self.username})"


class Permission(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    group_name = models.CharField(max_length=255)


class Role(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    permissions = models.ManyToManyField(Permission, related_name="roles")
