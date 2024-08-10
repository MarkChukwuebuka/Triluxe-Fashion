from django.contrib.auth import authenticate, login
from email_validator import validate_email

from account.models import User
from services.util import CustomRequestUtil


class UserService(CustomRequestUtil):
    def create_single(self, payload, is_staff=False):
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

        user, is_created = User.objects.create(
            email=email,
            last_name=last_name,
            first_name=first_name,
            password=password
        )

        return user, None

    def find_user_by_email(self, email):
        user = User.objects.prefetch_related("roles").filter(email__iexact=email).first()
        if not user:
            return None, self.make_error(f"User with email '{email}' not found")

        return user, None

