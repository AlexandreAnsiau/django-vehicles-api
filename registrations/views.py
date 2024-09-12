from django.contrib.auth.decorators import login_not_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import PasswordCreationFrom


class CustomLoginView(LoginView):
    template_name = "registrations/login.html"


@login_not_required
class PasswordCreationView(FormView):
    template_name = "registrations/password_creation.html"
    form_class = PasswordCreationFrom
    success_url = reverse_lazy("admin:login")

    def form_valid(self, form):
        return super().form_valid(form)



