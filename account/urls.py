from django.urls import path

from account.views import UserLoginView, UserSignupView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('signup/', UserSignupView.as_view(), name="signup"),
]
