from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('cart',views.list_cart,name='cart'),
    path('orders',views.list_orders,name='orders'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('remove/<pk>',views.remove,name='remove'),
    path('checkout',views.checkout,name='checkout'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)