from django.urls import path
from .views import  order_list, define_order, approve_order

urlpatterns = [
    path('get_orders/', order_list),
    path('define_order/', define_order),
    path('approve_order/', approve_order)
]