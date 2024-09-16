from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _


class PasswordCreationEmail:
    template_name = "registrations/emails/password_creation.html"
    subject = f"{settings.PROJECT_NAME}: {_('Création de votre mot de passe')}"

    def __init__(self, to, token):
        self.to = to
        self.token = token

    def send(self, *args, **kwargs):
        html_context = {"host": settings.HOST, "token": self.token.key}
        html_message = render_to_string(self.template_name, html_context)
        plain_message = strip_tags(html_message)
        send_mail(self.subject, plain_message, settings.TO_EMAIL, [self.to], html_message=html_message)


class PasswordResetEmail:
    template_name = "registrations/emails/password_reset.html"
    subject = f"{settings.PROJECT_NAME}: {_('Modification de votre mot de passe')}"

    def __init__(self, to, token):
        self.to = to
        self.token = token

    def send(self, *args, **kwargs):
        html_context = {"host": settings.HOST, "token": self.token.key}
        html_message = render_to_string(self.template_name, html_context)
        plain_message = strip_tags(html_message)
        send_mail(self.subject, plain_message, settings.TO_EMAIL, [self.to], html_message=html_message)
        

    

