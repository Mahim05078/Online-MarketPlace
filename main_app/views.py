from django.views.generic import TemplateView
from django.views import generic
from django.views.generic import ListView
from .models import Shop
from . import forms
from .models import RequestedRent, Shop
from django.shortcuts import render, redirect
from django.contrib import messages


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


def application(request):

    if request.method == "POST":
        apply_form = forms.applyform(request.POST)
        # print(print(request.POST.get("password")))
        if request.POST.get('Email') and request.POST.get('name') and request.POST.get('Contact'):
            if request.POST.get('NID') and request.POST.get('address'):
                customer = RequestedRent()
                shop = Shop.objects.filter(shopid=(int('0' + request.POST.get('shopid')))).first()
                customer.NID = request.POST.get('NID')
                customer.shop_id = shop
                customer.name = request.POST.get('name')
                customer.dob = request.POST.get('date')
                customer.email = request.POST.get('Email')
                customer.mobile = request.POST.get('Contact')
                customer.address = request.POST.get('address')
                customer.is_granted = 0
                customer.paid = 0
                customer.save()

                # return render(request, 'login.html', {'loginform': login_form})
                return redirect("http://127.0.0.1:8000/")

            else:
                print("error2")
                messages.error(request, "Password or credit card empty")
                # raise forms.ValidationError("")
        else:
            print("error3")
            messages.error(request, "Please give required field")

    return render(request, 'application.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def shoplisttorent(request):

    id = request.path
    print(id)
    shops = Shop.objects.filter(bookedStatus=0)
    return render(request, 'Shoplisttorent.html', {'shops': shops})
