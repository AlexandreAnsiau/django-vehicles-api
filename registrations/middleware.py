from django.shortcuts import redirect, reverse
from django.urls import resolve


class LoginMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        resolved_path = resolve(request.path)

        login_url_name = "login"

        is_url_authorised = (resolved_path.url_name == login_url_name or resolved_path.app_name == "admin")

        if not request.user.is_authenticated and not is_url_authorised:
            return redirect(reverse(login_url_name))

        return response