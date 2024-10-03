from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class homepage(TemplateView):
    """
    Display Home Page
    """
    template_name = 'home.html'
