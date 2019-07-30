from django import forms
from .models import User_Login, Shopowner
import hashlib


class login_form(forms.Form):

    name = forms.CharField(widget=forms.TextInput(
        attrs={'label': 'Username', 'class': 'form-control', 'placeholder': 'Enter Name'}))
    password = forms.CharField(label='Password', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'type': 'password'}))

    def clean(self, *args, **kwargs):
        print("I am here")
        user_name = self.cleaned_data.get("name")
        user_password = self.cleaned_data.get("password")

        user_obj = Shopowner.objects.filter(owner_id=user_name).first()
        # print(user_obj.user_pass)
        if not user_obj:
            raise forms.ValidationError("Invalid Username")

        else:
            p = hashlib.sha256(user_password.encode('utf-8')).hexdigest()
            if user_obj.owner_password != p:
                raise forms.ValidationError(
                    "Password Does not Match with username")

        return user_name
