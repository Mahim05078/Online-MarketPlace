from django.shortcuts import render
from . import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main_app.models import Customer
from login_app.forms import loginform
from django.contrib import messages

# Create your views here.


def register(request):
    login_form = loginform()
    if request.method == "POST":
        # register_form = forms.registerform(request.POST)
        # print(print(request.POST.get("password")))
        if request.POST.get('Email') and request.POST.get('name') and request.POST.get('Contact'):
            if request.POST.get('Password') == request.POST.get('ConfirmPassword'):
                if request.POST.get('Password') and request.POST.get('creditno'):
                    customer = Customer()
                    customer.cust_name = request.POST.get('name')
                    customer.cust_contact = request.POST.get('Contact')
                    customer.cust_dob = request.POST.get('date')
                    customer.cust_email = request.POST.get('Email')
                    customer.cust_creditno = request.POST.get('creditno')
                    customer.cust_password = request.POST.get('Password')
                    customer.cust_Address = request.POST.get('address')
                    customer.save()
                    # return render(request, 'login.html', {'loginform': login_form})
                    return redirect("http://127.0.0.1:8000/login.html")
                else:
                    print("error1")
                    messages.error(request, "Password doesn't match")
                #     raise forms.ValidationError("Password doesn't match")
            else:
                print("error2")
                messages.error(request, "Password or credit card empty")
                # raise forms.ValidationError("")
        else:
            print("error3")
            messages.error(request, "Please give required field")

    return render(request, 'register.html')