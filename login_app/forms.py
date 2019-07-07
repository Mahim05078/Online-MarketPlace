from django import forms
from .models import Customer



class loginform(forms.Form):

    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email', 'type': 'email'}))
    password = forms.CharField(label='Password', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'type': 'password'}))

    def clean(self, *args, **kwargs):
        print("I am here")
        cust_email = self.cleaned_data.get("email")
        cust_password = self.cleaned_data.get("password")
        print(cust_password)
        user_obj = Customer.objects.filter(cust_email=cust_email).first()
        # print(user_obj.user_pass)
        if not user_obj:
            raise forms.ValidationError("Invalid email")
        else:
            if user_obj.cust_password != cust_password:
                raise forms.ValidationError(
                    "Invalid Password. Please try again.")

        return cust_email

