from django.shortcuts import render
from django.views import View

from account.services.auth_service import AuthService
from account.services.user_service import UserService
from services.util import CustomRequestUtil


class UserLoginView(View, CustomRequestUtil):
    template_name = 'login.html'
    extra_context_data = {
        "title": "Sign In",
    }

    def get(self, request, *args, **kwargs):
        return self.process_request(request)

    def post(self, request, *args, **kwargs):
        auth_service = AuthService(self.request)

        self.template_name = None
        self.template_on_error = 'login.html'

        payload = {
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
        }

        return self.process_request(
            request, target_view="dashboard", target_function=auth_service.login, payload=payload
        )


class UserSignupView(View, CustomRequestUtil):
    template_name = 'signup.html'
    extra_context_data = {
        "title": "Sign Up",
    }

    def get(self, request, *args, **kwargs):
        return self.process_request(request)

    def post(self, request, *args, **kwargs):
        user_service = UserService(self.request)

        self.template_name = None
        self.template_on_error = 'signup.html'

        payload = {

            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'first_name': request.POST.get('first-name'),
            'last_name': request.POST.get('last-name'),
        }

        return self.process_request(
            request, target_view="dashboard", target_function=user_service.create_single, payload=payload
        )
