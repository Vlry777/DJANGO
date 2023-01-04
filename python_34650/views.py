
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def index(request):
    return render(request,'index.html', context={})
    
def hola_mundo(request):
    return HttpResponse('hola mundo')

def otra_mas(request):
    return HttpResponse('si otra mas')

def fecha_actual(request):
    hoy = datetime.now().date()
    return HttpResponse(f'la fecha de hoy es {hoy}')

def vista_con_edad(request,edad):
    return HttpResponse(f'esto funciona? la edad es {edad}?')

def vista_con_template(request):
    return render(request, 'template.html', context={})

def saludo_desde_template(request):
    context = {
        'nombre': 'Camila',
        'edad': 18,
        'usa_lentes': False,
        'lista_frutas': ['banana','manzana', 'pera', 'anana']
    }
    return render(request, 'saludo.html', context= context)

