from django.forms import forms

class ExampleForm(forms.Form):
    customuser = forms.CharField(max_length=100)

