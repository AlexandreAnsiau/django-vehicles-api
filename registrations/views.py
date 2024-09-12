from django.contrib.auth.decorators import login_not_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import PasswordCreationFrom
from .models import ResetPasswordToken


class CustomLoginView(LoginView):
    template_name = "registrations/login.html"


@login_not_required
class PasswordCreationView(FormView):
    template_name = "registrations/password_creation.html"
    form_class = PasswordCreationFrom
    success_url = reverse_lazy("admin:login")

    def form_valid(self, form):
        token = ResetPasswordToken.objects.get(key=form.cleaned_data.get("token"))
        token.user.set_password(form.cleaned_data.get("password"))
        token.user.save()
        token.delete()
        return super().form_valid(form)



