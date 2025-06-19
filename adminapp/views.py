from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.

from  .form import ContactForm
# from  django.contrib.auth.models import User


from django.contrib.auth import get_user_model


User = get_user_model()



def forms(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
    
        if form.is_valid():

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']

            user= User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)

            user.is_staff = True     # ✅ Required to allow admin access
            user.role == 'brand_admin'
            user.save()
            return redirect('/admin/')
        

    else:
        message = "error"
        form = ContactForm()

                        
    return render(request,'index.html',{'form' :form})


