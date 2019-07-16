from django import forms


class applyform(forms.Form):

    def clean(self, *args, **kwargs):
        print("I am here")
