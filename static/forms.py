from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='account_name', max_length=10)
