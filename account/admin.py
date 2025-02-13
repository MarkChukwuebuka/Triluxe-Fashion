from django.contrib import admin

from account.models import User, Role, Profile
from crm.admin import BaseAdmin
from django.templatetags.static import static



admin.site.site_header = 'Triluxe'
admin.site.site_title = 'Triluxe'
admin.site.index_title = 'Triluxe Admin'

# Register your models here.

@admin.register(Role)
class RoleAdmin(BaseAdmin):
    list_display = ["name"] + BaseAdmin.list_display
    search_fields = ["name"]


@admin.register(User)
class UserAdmin(BaseAdmin):
    list_display = ["email", "first_name", "last_name"] + BaseAdmin.list_display
    search_fields = ["email", "first_name", "last_name"]
    readonly_fields = ["password"] + BaseAdmin.readonly_fields
    list_filter = ["user_type"]
    autocomplete_fields = ["roles"] + BaseAdmin.autocomplete_fields


@admin.register(Profile)
class ProfileAdmin(BaseAdmin):
    list_display = ["user", "phone", "city", "state"]
    search_fields = ["user", "city", "state", "address"]
    list_filter = ["city", "state"]

