from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class HomeView(TemplateView):
    """
    Class-based view for rendering the home page.
    """
    template_name = 'home/welcome.html'



class LoginInterfaceLoginView(LoginView):
    template_name = 'home/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)
    