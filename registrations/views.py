from django.contrib import messages
from django.contrib.auth.decorators import login_not_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from .emails import PasswordResetEmail
from .forms import PasswordResetRequestForm, PasswordSetFrom
from .models import CustomUser, ResetPasswordToken


class CustomLoginView(LoginView):
    template_name = "registrations/login.html"


class PasswordSetView(FormView):
    form_class = PasswordSetFrom
    success_url = reverse_lazy("admin:login")

    def form_valid(self, form):
        token = ResetPasswordToken.objects.get(key=form.cleaned_data.get("token"))
        token.user.set_password(form.cleaned_data.get("password"))
        token.user.save()
        token.user.resetpasswordtoken_set.update(is_actif=False)
        messages.add_message(self.request, messages.SUCCESS, _("Votre password a été enregistré."))
        return super().form_valid(form)


@login_not_required
class PasswordCreationView(PasswordSetView):
    template_name = "registrations/password_creation.html"


@login_not_required
class PasswordResetView(PasswordSetView):
    template_name = "registrations/password_reset.html"


@login_not_required
class PasswordResetRequestView(FormView):
    form_class = PasswordResetRequestForm
    template_name = "registrations/password_reset_request.html"
    success_url = reverse_lazy("password_reset")

    def form_valid(self, form):
        user = CustomUser.objects.filter(email=form.cleaned_data.get("email")).first()
        token = ResetPasswordToken.objects.create(user=user)
        PasswordResetEmail(user.email, token).send()
        messages.add_message(self.request, messages.SUCCESS, _("Un mail vous a été envoyé contenant un lien vous permettant de changer votre mot de passe."))
        return super().form_valid(form)



