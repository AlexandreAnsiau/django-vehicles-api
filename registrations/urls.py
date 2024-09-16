from django.urls import path

from .views import CustomLoginView, PasswordCreationView, PasswordResetRequestView, PasswordResetView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("password-creation/", PasswordCreationView.as_view(), name="password_creation"),
    path("password-reset-request/", PasswordResetRequestView.as_view(), name="password_reset_request"),
    path("password-reset/", PasswordResetView.as_view(), name="password_reset"),
]