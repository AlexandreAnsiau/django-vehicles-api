from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = "registrations/login.html"