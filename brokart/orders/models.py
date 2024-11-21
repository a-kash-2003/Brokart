from django.db import models
from customers.models import Customers
from products.models import Products

# Data model for order
class Order(models.Model):
    LIVE=1
    DELETE=0    
    DELETE_CHOICE=((LIVE,'live'),(DELETE,'delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    ORDER_CHOICE=((ORDER_PROCESSED,'ORDER_PROCESSED'),
                  (ORDER_DELIVERED,'ORDER_DELIVERED'),
                  (ORDER_REJECTED,'ORDER_REJECTED'))
    order_status=models.IntegerField(choices=ORDER_CHOICE,default=CART_STAGE)
    total_price=models.FloatField(default=0)
    owner=models.ForeignKey(Customers,on_delete=models.SET_NULL,related_name='orders',null=True)
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return 'order-{}-{}'.format(self.id,self.owner.name)

# model for ordered itmes
class Order_Items(models.Model):
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,related_name='added_carts',null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')

    def __str__(self) -> str:
        return self.name