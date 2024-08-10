from django.contrib.auth import authenticate, login
from services.util import CustomRequestUtil


class AuthService(CustomRequestUtil):
    def login(self, payload):
        email = payload.get("email")
        password = payload.get("password")

        user = authenticate(self.request, email=email, password=password)

        if not user:
            return None, self.make_error("Email/Password is not correct!")

        login(self.request, user)

        return user, None

    def signup(self, payload):
        email = payload.get("email")
        first_name = payload.get("first-name")
        last_name = payload.get("last-name")
        password = payload.get("password")

        user = authenticate(self.request, email=email, password=password)

        if not user:
            return None, self.make_error("Email/Password is not correct!")

        login(self.request, user)

        return user, None
