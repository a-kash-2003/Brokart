from django import template

register=template.Library()
@register.simple_tag(name='total')
def total(cart):
    SubTotal=0
    for item in cart.added_items.all():
        SubTotal+=item.quantity*item.product.price
        Tax=3*SubTotal/100
        Total=Tax+SubTotal
    return Total