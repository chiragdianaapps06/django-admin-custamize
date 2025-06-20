from django.urls import path 

from . import views

urlpatterns = [
    path("",views.forms,name = "forms"),
    path("home/",views.home,name ='home')
]

