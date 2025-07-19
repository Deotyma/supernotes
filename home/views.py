from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

class HomeView(TemplateView):
    """
    Class-based view for rendering the home page.
    """
    template_name = 'home/welcome.html'



class LoginInterfaceLoginView(LoginView):
    template_name = 'home/login.html'


class LoginInterfaceLogoutView(LogoutView):
    template_name = 'home/logout.html'