from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Profile
from math import ceil
import json
from django.views.generic import View
from django.shortcuts import redirect
# Create your views here.

def encode(request):
    return render(request,'shop/encode.html');
def decode(request):
    return render(request,'shop/decode.html')
def index(request):
    return render(request, 'shop/dashboard.html')
def about(request):
    return render(request, 'shop/about.html')


class Handlelogin(View):
    def get(self,request,*args,**kwargs):
        account = True
        return render(request, "shop/login.html", {"account": account})
    def post(self,request,*args,**kwargs):
        
        username = request.POST['Username']
        password = request.POST['passwordlogin']
        user = authenticate(username=username, password=password)

        print(user)
        if user is not None:
            login(request, user)
        
            messages.success(request, 'Login Succesfully')
            account = True

            return render(request, "shop/about.html", {"account": account, "username": user})
        else:
            account = False
            return render(request, "shop/login.html", {"account": account})

class Handlesignup(View):
    def get(self,request,*args,**kwargs):
        return render(request, "shop/signup.html")

    def post(self,request,*args,**kwargs):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

  
       
        try:

            myuser = User.objects.create_user(username, email, password)
            profileuser = Profile(phone=phone,user=myuser)
            profileuser.save()
            login(request, myuser)

            messages.success(request, "Account Created")
            success = True
            print("signup.......")
            return render(request, "shop/about.html", {"Account": success})

        except:
            return render(request, "shop/signup.html", {"Account": True})



class Handlelogout(View):
    def post(self,request,*args,**kwargs):
       
        return render(request, "shop/login.html", {"account":True,"logout": True});
    def get(self,request,*args,**kwargs):
        
        datas = Profile.objects.get(user=request.user)
        datas.save()
    
        logout(request)
        logoutt = True
        account=True
        print("logout1.......")
        return render(request, "shop/login.html", {"account":True,"logout": True});
