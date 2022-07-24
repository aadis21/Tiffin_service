"""Tiffin_Service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from all_functions import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),

    path("adminlogin", adminlogin),
    path("addadmin", addadmin),
    path("viewadmin", viewadmin, name='viewadmin'),
    path("deleteadmin", deleteadmin),
    path("editadmin", editadmin),
    path("saveadmin", saveadmin),
    path("adminlogout", adminlogout),
    path("adminDashboard", adminDashboard),

    path("addarea", addarea),
    path("viewarea", viewarea),
    path("deletearea", deletearea),
    path("editarea", editarea),
    path("savearea", savearea),

    path("addmenu", addmenu),
    path("viewmenu", viewmenu),
    path("deletemenu", deletemenu),
    path("editmenu", editmenu),
    path("savemenu", savemenu),

    path("usersignup", usersignup, name="usersignup"),
    path("personaldetails", personaldetails),
    path("deliveryareas", deliveryareas, name="deliveryareas"),
    path("userlogin", userlogin, name="userlogin"),
    path("usersubscription", user_subscription, name="usersubscription"),
    path("userdashboard", userdashboard, name="userdashboard"),
    path("changeuserpassword", changeuserpassword),
    path("userlogout", userlogout, name="userlogout"),

    path("userbooking", userbooking),
    path("checkout", checkout),
    path("paymentsuccess", paymentsuccess, name="paymentsuccess"),
    # path("thankspage", thankspage),

    path("aboutus", aboutus, name="aboutus"),
    path("whyus", whyus, name="whyus"),
    path("howitworks", howitworks, name="howitworks"),
    path("changeuserdetails", changeuserdetails, name="changeuserdetails"),
    path("changeuserpassword", changeuserpassword, name="changeuserpassword"),

    # path("paymentaction", paymentAction, name="paymentAction"),

]
