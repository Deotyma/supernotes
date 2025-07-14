from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView

class HomeView(TemplateView):
    """
    Class-based view for rendering the home page.
    """
    template_name = 'home/welcome.html'
    #extra_context = {'today':datetime.today()}


