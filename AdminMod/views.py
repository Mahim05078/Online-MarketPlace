from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main_app.models import Shop, RequestedRent, Shopowner, Shopassigned
from django.conf import settings
from django.core.mail import send_mail
import datetime
import hashlib


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
    # send mail

    applications = RequestedRent.objects.all()
    if request.GET.get('email'):
        print("heere")
        url = request.get_full_path()
        id = url.split("=")[1]
        application = RequestedRent.objects.filter(NID=(int('0' + id))).first()
        id = application.shop_id.shopid
        application.is_granted = 1
        application.save()

        subject = 'Appointment'
        message = 'Thank you for apply to our market .Please come with 7 days upto 10.00 to 4.00. Office:Polashi,BUET'

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [application.email, ]
        send_mail(subject, message, email_from, recipient_list)

        return render(request, 'applicationview.html/', {'applications': applications})

    elif request.GET.get('grant'):
        url = request.get_full_path()
        id = url.split("=")[1]
        application = RequestedRent.objects.filter(NID=(int('0' + id))).first()

        shopowner = Shopowner()
        shopowner.owner_id = Shopowner.objects.all().count()+1
        shopowner.owner_name = application.name
        passwd = "1234"
        shopowner.owner_password = hashlib.sha256(
            passwd.encode('utf-8')).hexdigest()
        shopowner.owner_contact = application.mobile
        shopowner.owner_dob = application.dob
        shopowner.owner_email = application.email
        shopowner.owner_nid = application.NID
        shopowner.owner_Adress = application.address
        shopowner.num_shop = application.shop_id.shopid
        shopowner.owner_creditno = "23465"
        shopowner.save()

        shop = Shop.objects.filter(shopid=application.shop_id.shopid).first()
        shop.bookedStatus = 1
        shop.save()

        shopasg = Shopassigned()
        shopasg.owner_id = shopowner
        shopasg.shop_id = shop
        shopasg.remainPayment = 0
        # shopasg.expire_Date = datetime.date.today
        shopasg.save()

        subject = 'Shop Assignment'

        message = "your id is: "+str(shopowner.owner_id)+" and password is : " + str(
            passwd) + " Shop is : " + str(shopowner.num_shop)

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [shopowner.owner_email, ]
        send_mail(subject, message, email_from, recipient_list)

        application.delete()

        return render(request, 'applicationview.html/', {'applications': applications})

    return render(request, 'applicationview.html/', {'applications': applications})
