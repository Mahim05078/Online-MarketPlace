from django import forms
from .models import User_Login, Customer


class login_form(forms.Form):

    name = forms.CharField(widget=forms.TextInput(
        attrs={'label': 'Username', 'class': 'form-control', 'placeholder': 'Enter Name'}))
    password = forms.CharField(label='Password', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'type': 'password'}))

    def clean(self, *args, **kwargs):
        print("I am here")
        user_name = self.cleaned_data.get("name")
        user_password = self.cleaned_data.get("password")
        print(user_password)
        user_obj = User_Login.objects.filter(user_name=user_name).first()
        # print(user_obj.user_pass)
        if not user_obj:
            raise forms.ValidationError("Invalid Username")

        else:
            if user_obj.user_pass != user_password:
                raise forms.ValidationError(
                    "Password Does not Match with username")

        return user_name
