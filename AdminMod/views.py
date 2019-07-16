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


def shopEntry(request):
    Shop_form = forms.shopform(request.POST)
    if request.method == "POST":
        # register_form = forms.registerform(request.POST)
        # print(print(request.POST.get("password")))
        if request.POST.get('Id') and request.POST.get('name'):
            if request.POST.get('area') and request.POST.get('rentcost'):
                newShop = Shop()
                newShop.shopid = request.POST.get('Id')
                newShop.shopname = request.POST.get('name')
                newShop.bookedStatus = 0
                newShop.rentCost = request.POST.get('rentcost')
                newShop.area = request.POST.get('area')
                newShop.floor = request.POST.get('floor')
                newShop.save()
            else:
                print("error1")

            #     raise forms.ValidationError("Password doesn't match")

        else:
            print("error3")

    return render(request, 'Addshopform.html')


def Shopmanagement(request):
    shops = Shop.objects.all()
    return render(request, 'Shopmanagement.html/', {'shops': shops})


def Shopstatistics(request):
    shops = Shop.objects.all()
    return render(request, 'Shopstatistics.html/', {'shops': shops})


def tmp(request):
    #send mail
    applications = RequestedRent.objects.all()
    if request.GET.get('btn'):
        print("heere")
        return render(request, 'applicationview.html/', {'applications': applications})
    
    
    return render(request, 'applicationview.html/', {'applications': applications})
