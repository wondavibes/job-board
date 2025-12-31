from django.urls import path
from .views import (
    register_view,
    login_view,
    logout_view,
    candidate_dashboard,
    employer_dashboard,
)

from .views import home_view

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("", home_view, name="home"),
    path("candidate/dashboard", candidate_dashboard, name="candidate_dashboard"),
    path("employer/dashboard", employer_dashboard, name="employer_dashboard"),
]
