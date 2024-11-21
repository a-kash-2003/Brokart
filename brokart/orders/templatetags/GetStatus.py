from django import template

register=template.Library()
@register.simple_tag(name='GetStatus')
def GetStatus(status):
    status-=1
    status_list=['Comfirmed','Processed','Delivered','Rejected']
    return status_list[status]
