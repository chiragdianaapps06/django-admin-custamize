from django import forms
from .models import FormModel


class ContactForm(forms.Form):
    username = forms.CharField(max_length=40,error_messages={'required':"filll required filled"})
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    brandname = forms.CharField()

    # gender = [('M','male'),('F',"female")]
    # choice = forms.ChoiceField(choices=gender)
    # duration = forms.DecimalField()
    # colors = forms.MultipleChoiceField(choices=[('R', 'Red'), ('G', 'Green')])

    # pickcolor = forms.CharField(widget = forms.TextInput(attrs={'type':'color'}))
    

class   StudentForm(forms.ModelForm):
    
    class Meta:
        model = FormModel
        fields = ['name', 'age', 'email']
       
