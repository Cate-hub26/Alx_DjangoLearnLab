from django.forms import forms

class CustomUserForm(forms.Form):
    customuser = forms.CharField(max_length=100)

