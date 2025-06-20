from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.

from  .form import ContactForm
# from  django.contrib.auth.models import User
from django.contrib.auth.models import Group


from django.contrib.auth import get_user_model

from .models import Brand


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
            brandname = form.cleaned_data['brandname']
          
            brandname = form.cleaned_data['brandname']
            brand_instance, created = Brand.objects.get_or_create(name=brandname)

            user= User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password,)

            user.is_staff = True     # ✅ Required to allow admin access
            user.role = 'brand_admin'
            user.brand = brand_instance 
            # user.groups == 'brand_admin'
            group, created = Group.objects.get_or_create(name='brand_Admin')
            user.groups.add(group)
            user.save()
            
            return redirect('/admin/')
        

    else:
        message = "error"
        form = ContactForm()

                        
    return render(request,'index.html',{'form' :form})

from .form import StudentForm
def home(request):
  
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form': form})



