from django.shortcuts import render,redirect
from . models import Customers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def log_out(request):
     logout(request)
     return redirect('home')
def list_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            #user account creation
            user=User.objects.create_user(
                username=username,
                email=email,
                password=password
                )
            #crstomer account creation
            customer=Customers.objects.create(
                user=user,
                phone=phone,
                address=address
                )
            success_message="Successfully Registered"
            messages.success(request,success_message)
        except Exception as e:
                error_message="Username already exists."
                messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
             login(request,user)
             return redirect('home')
        else:
             messages.error(request,'Invalid Credentials')

    return render(request,'account.html',context)