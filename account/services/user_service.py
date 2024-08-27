from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from email_validator import validate_email

from account.models import User
from services.util import CustomRequestUtil


class UserService(CustomRequestUtil):
    def create_single(self, payload):
        """Payload requirements:
        {
        email: String,
        password: String,
        first_name: String,
        last_name: String
        }
        """

        email = payload.get("email")
        password = payload.get("password")
        first_name = payload.get("first_name")
        last_name = payload.get("last_name")

        try:
            email_info = validate_email(email, check_deliverability=True)
            email = email_info.normalized
        except Exception as e:
            return None, self.make_error("Please enter a valid email address")

        existing_user, _ = self.find_user_by_email(email)
        if existing_user:
            return None, self.make_error("User with email already exist")

        user, is_created = User.objects.get_or_create(
            email=email,
            defaults=dict(
                last_name=last_name,
                first_name=first_name,
                password=make_password(password)
            )
        )

        if not is_created:
            return None, self.make_error("User already exist")

        return user, None

    def find_user_by_email(self, email):
        user = User.objects.prefetch_related("roles").filter(email__iexact=email).first()
        if not user:
            return None, self.make_error(f"User with email '{email}' not found")

        return user, None

    def update_single(self, payload):
        user = self.auth_user
        user.first_name = payload.get('first_name', user.first_name)
        user.last_name = payload.get('last_name', user.last_name)
        user.phone = payload.get('phone', user.phone)

        current_password = payload.get('current_password')
        new_password = payload.get('new_password')
        confirm_password = payload.get('confirm_password')



        return message, None

