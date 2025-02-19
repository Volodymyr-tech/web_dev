from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import RegisterView, UpdateCustomUser, email_verification, UserLoginView

app_name = "users"

urlpatterns = [
    path("login/", UserLoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="catalog:home"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("email-verification/<str:token>/", email_verification, name="email-confirm"),
    path("update-user/<int:pk>/", UpdateCustomUser.as_view(), name="update-user"),
]
