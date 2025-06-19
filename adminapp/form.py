from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(max_length=40)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

