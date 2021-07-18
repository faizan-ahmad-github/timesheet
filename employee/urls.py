from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path("signup/", views.CustomSignUp.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("", views.CustomLoginView.as_view(), name="login"),
    path("home/", views.HomeView.as_view(), name="home"),

    path("inTime/", views.clockIn, name="log_time"),
    path("pauseTime/", views.clockPause, name="log_pause"),
    path("outTime/", views.clockStop, name="log_stop"),
]
