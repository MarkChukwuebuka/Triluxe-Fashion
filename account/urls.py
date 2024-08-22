from django.urls import path

from account.views import UserLoginView, UserSignupView, UserDashboardView, UserLogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('signup/', UserSignupView.as_view(), name="signup"),

    path('dashboard/', UserDashboardView.as_view(), name="dashboard"),
]
