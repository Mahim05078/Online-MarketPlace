from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Shop
# from . import forms
from django.shortcuts import render, redirect


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = " Nazmul Hasan"
        context['country'] = "Bangladesh"

        list = [1, 2, 3]
        context['list'] = list
        return context


class AboutView(TemplateView):
    template_name = "about.html"


class registerView(TemplateView):
    template_name = "register.html"


def index(request):
    return render(request, 'index.html', {})
