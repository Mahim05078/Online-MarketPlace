from django import forms
from main_app.models import Customer


class registerform(forms.Form):
    # username = forms.CharField(label="Name", required=True, max_length=30,
    #                            widget=forms.TextInput(attrs={
    #                                'class': 'form-control',
    #                                'name': 'Name'}))
    # email = forms.EmailField(label='Email', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter Email', 'type': 'email'}))
    # password = forms.CharField(label='Password', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'type': 'password'}))
    # repassword = forms.CharField(label='Re-password', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Re-enter Password', 'type': 'password'}))

    def clean(self, *args, **kwargs):
        print("I am here")
    #     cust_email = self.cleaned_data.get("email")
    #     cust_password = self.cleaned_data.get("password")
    #     print(cust_password)
    #     user_obj = Customer.objects.filter(cust_email=cust_email).first()
    #     # print(user_obj.user_pass)
    #     if not user_obj:
    #         raise forms.ValidationError("Invalid email")
    #     else:
    #         if user_obj.cust_password != cust_password:
    #             raise forms.ValidationError(
    #                 "Invalid Password. Please try again.")

    #     return cust_email
