from django.shortcuts import render,redirect
from .models import Order,Order_Items
from products.models import Products
from django.contrib import messages
from customers.models import Customers

# Create your views here.

def list_cart(request):
    user=request.user
    customer=user.customer_profile
    quantity=request.POST.get('quantity')
    product_id=request.POST.get('product_id')
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context={'cart':cart_obj}
    return render(request,'cart.html',context)

def list_orders(request):
    user=request.user
    customer=user.customer_profile
    order_obj=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':order_obj}
    return render(request,'orders.html',context)

def remove(request,pk):
    item=Order_Items.objects.get(pk=pk)
    item.delete()
    return redirect('cart')

def checkout(request):
    if request.POST:
        try:
            user=request.user
            customer=user.customer_profile
            total=float(request.POST.get('total'))
            order_obj=Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status=Order.ORDER_CONFIRMED
                order_obj.total_price=total
                order_obj.save()
                status_message="Your order is processed and will be delivered within 3 Days."
                messages.success(request,status_message)
            else:
                status_message="Unable to process, no items in cart!"
                messages.error(request,status_message)
        except Exception as e:
            status_message="Unable to process, no items in cart!"
            messages.error(request,status_message)
    return redirect('cart')

def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product=Products.objects.get(pk=product_id)
        ordered_item,Created=Order_Items.objects.get_or_create(
            product=product,
            owner=cart_obj
        )
        if Created:
            ordered_item.quantity=quantity
            ordered_item.save()
        else:
            ordered_item.quantity+=quantity
            ordered_item.save()
        return redirect('cart')