from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def products_list(request):
    return render(request,'products.html')

def product_details(request):
    return render(request,'product_details.html')