from django.db import models
from django.utils import timezone


class AvailableManager(models.Manager):
    def get_queryset(self):
        return (
            super(AvailableManager, self)
            .get_queryset()
            .filter(deleted_at__isnull=True)
        )


class ActiveManager(models.Manager):
    def get_queryset(self):
        return (
            super(ActiveManager, self)
            .get_queryset()
            .filter(deactivated_at__isnull=True)
        )


class ObjectManager(models.Manager):
    def get_queryset(self):
        return super(ObjectManager, self).get_queryset()


class ActiveAvailableManager(models.Manager):
    def get_queryset(self):
        return (
            super(ActiveAvailableManager, self)
            .get_queryset()
            .filter(deactivated_at__isnull=True, deleted_at__isnull=True)
        )


class AppDbModel(models.Model):
    objects = ObjectManager()

    class Meta:
        abstract = True


class BaseModel(AppDbModel):
    deactivation_reason = models.TextField(null=True, blank=True)
    deactivated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey(
        "account.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    updated_by = models.ForeignKey(
        "account.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    deleted_by = models.ForeignKey(
        "account.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    deactivated_by = models.ForeignKey(
        "account.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )

    active_available_objects = ActiveAvailableManager()
    active_objects = ActiveManager()
    available_objects = AvailableManager()

    class Meta:
        abstract = True


class ActivityLog(AppDbModel):
    user = models.ForeignKey(
        "account.User",
        on_delete=models.CASCADE,
        related_name="user_activities",
    )
    activity_type = models.CharField(max_length=255, null=True)
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} by {} - {}".format(self.activity_type, self.user, self.note)


class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7, null=True, blank=True)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_on = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email