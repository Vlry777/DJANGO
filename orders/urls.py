from django.urls import path

from orders.views import list_orders,create_orders

urlpatterns = [
    path('list-orders/',list_orders),
    path('create-orders/',create_orders),
]