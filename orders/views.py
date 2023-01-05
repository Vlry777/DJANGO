from django.shortcuts import render
from django.http import HttpResponse

from orders.models import Order

def list_orders(request):
    orders = Order.objects.all()
    context = {
        'orders' : orders,
    }
    return render(request, 'orders/list_orders.html', context=context)

def create_orders(request):
    Order.objects.create(client= 'Lara', product='Curso de PYTHON',payment_method= 'Card')
    return HttpResponse('Order create')

