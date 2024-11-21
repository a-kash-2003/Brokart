from django import template

register=template.Library()
@register.simple_tag(name='tax')
def tax(cart):
    total=0
    for item in cart.added_items.all():
        total+=item.quantity*item.product.price
        Tax=3*total/100
    return Tax