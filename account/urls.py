from django.urls import path

from account.views import  UserSignupView, UserDashboardView, UserLogoutView, UpdateUserView, login_view
from django.contrib.auth.views import LoginView  # Import Django's built-in LoginView

urlpatterns = [
    # path('login/', UserLoginView.as_view(), name="login"),
 path('login/', login_view, name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('signup/', UserSignupView.as_view(), name="signup"),

    path('dashboard/', UserDashboardView.as_view(), name="dashboard"),
    path('settings/', UpdateUserView.as_view(), name="settings"),
]
