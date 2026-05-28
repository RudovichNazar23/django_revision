from django.urls import path
from .views import welcome_page, main_page, login_user, logout_user

urlpatterns = [
    path("", welcome_page, name="welcome_page"),
    path("main_page/", main_page, name="main_page"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout")
]
