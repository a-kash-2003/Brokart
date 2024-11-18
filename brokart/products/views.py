from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_products=Products.objects.order_by('priority')[:4]
    latest_products=Products.objects.order_by('-id')[:8]
    context={'featured_products':featured_products,
             'latest_products':latest_products}
    return render(request,'index.html',context)

def products_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    p_list=Products.objects.order_by('priority')
    Paginator_list=Paginator(p_list,4)
    p_list=Paginator_list.get_page(page)
    context={'products':p_list}
    return render(request,'products.html',context)

def product_details(request,pk):
    product=Products.objects.get(pk=pk)
    context={'product':product}
    return render(request,'product_details.html',context)