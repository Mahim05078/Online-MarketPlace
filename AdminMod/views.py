from django.shortcuts import render
from . import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.


def login(request):
    login_form = forms.login_form()
    if request.method == "POST":
        login_form = forms.login_form(request.POST)
        # print(print(request.POST.get("password")))
        if login_form.is_valid():
            # print(request.POST)
            return redirect('http://127.0.0.1:8000/admin/')

    return render(request, 'Login.html', {'login_form': login_form})
