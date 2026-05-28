from django.http import HttpRequest
from django.shortcuts import redirect


class WelcomePagePermissionMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self._get_response(request)

        if request.method == "GET" and request.path == "/main_page/":
            if request.user.is_authenticated:
                return response
            return redirect("/")
        return response
