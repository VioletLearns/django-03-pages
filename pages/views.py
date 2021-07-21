# from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class VioletPageView(TemplateView):
    template_name = 'Violet.html'

class AnotherPageView(TemplateView):
    template_name = 'another_page.html'