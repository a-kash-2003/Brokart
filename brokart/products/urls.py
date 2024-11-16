
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('product_list',views.list_products,name='list_products'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)