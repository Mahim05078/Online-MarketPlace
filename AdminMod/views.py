from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main_app.models import Shop, RequestedRent

# Create your views here.


class AdminView(TemplateView):
    template_name = "admin.html"


def login(request):
    login_form = forms.login_form()
    if request.method == "POST":
        login_form = forms.login_form(request.POST)
        # print(print(request.POST.get("password")))
        if login_form.is_valid():
            # print(request.POST)
            return redirect('http://127.0.0.1:8000/gotoadmin/admin.html/')

    return render(request, 'Login.html', {'login_form': login_form})


def applicationview(request):
    applications = RequestedRent.objects.all()
    return render(request, 'applicationview.html/', {'applications': applications})


def Shopmanagement(request):
    shops = Shop.objects.all()
    return render(request, 'Shopmanagement.html/', {'shops': shops})


def Shopstatistics(request):
    shops = Shop.objects.all()
    return render(request, 'Shopstatistics.html/', {'shops': shops})
