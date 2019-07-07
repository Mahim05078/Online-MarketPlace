from django.shortcuts import render
from . import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.


def login(request):
    login_form = forms.loginform()
    if request.method == "POST":

        login_form = forms.loginform(request.POST)
        # print(print(request.POST.get("password")))
        if login_form.is_valid():
            # print(request.POST)

            return redirect("http://127.0.0.1:8000/#")

    return render(request, 'login.html', {'loginform': login_form})
