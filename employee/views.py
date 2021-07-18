from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render


from .models import logtime
import datetime as datetime
import time


log_time = 0
pause_time = 0
end_time = 0
total_time = 0


def start_logging():
    global log_time, pause_time, total_time
    month = year = datetime.date.today().month
    log_time = datetime.datetime.utcnow().today()
    if pause_time != 0:
        time_delta = (pause_time - log_time)
        total_seconds = time_delta.total_seconds()
        total_seconds = total_seconds/60
        minutes = total_seconds / 60
        hours = minutes / 60
        total_time = total_time - hours
        total_time = total_time/60
        total_time = total_seconds
        print('Session resterted. Total Time: ', total_time)
        return total_time
    # time.sleep(15)
    return log_time


def pause_logging():
    global log_time, total_time, pause_time
    pause_time = datetime.datetime.today()
    time_delta = (pause_time - log_time)
    total_seconds = time_delta.total_seconds()
    total_seconds = total_seconds/60
    minutes = total_seconds / 60
    hours = minutes / 60
    # Assigning hours to total time so that end_log can access it and append it.
    total_time = total_seconds
    return total_time


def end_log():
    global log_time, total_time, end_time
    end_time = datetime.datetime.today()
    time_delta = (end_time - log_time)
    total_seconds = time_delta.total_seconds()
    total_seconds = total_seconds/60
    minutes = total_seconds / 60
    hours = minutes / 60
    # Assigning hours to total time so that end_log can access it and append it.
    total_time = total_seconds
    return total_time


class HomeView(TemplateView):
    Model = logtime
    template_name = "home.html"


class CustomLoginView(LoginView):

    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = (True)

    def get_success_url(self):
        return reverse_lazy("home")


class CustomSignUp(FormView):
    template_name = "signup.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomSignUp, self).form_valid(form)


def clockIn(request):
    logged = request.POST.get(clockIn)
    print("log_time triggered")
    start_logging()
    print(log_time)
    return render(request, "home.html")


def clockPause(request):
    log_pause = request.POST.get(clockPause)
    print("log_pause triggered")
    pause_logging()
    print(total_time)
    return render(request, "home.html")


def clockStop(request):
    log_stop = request.POST.get(clockStop)
    print("log_stop triggered")
    end_log()
    print("Total logged in time:", total_time)
    return render(request, "home.html")
