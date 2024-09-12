from django.urls import path

from .views import PasswordCreationView, CustomLoginView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("password_creation", PasswordCreationView.as_view(), name="password_creation")
]