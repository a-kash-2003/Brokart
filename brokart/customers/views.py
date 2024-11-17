from django.shortcuts import render

# Create your views here.

def list_account(request):
    return render(request,'account.html')