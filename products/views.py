from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products, Category


def create_product(request):
    if request.method == 'GET':
        return render(request,'products/create_product.html',context={})
        
    elif request.method == 'POST':
        Products.objects.create(name = request.POST['name'], price = request.POST['price'])
        return render(request,'products/create_product.html',context={})

def list_products(request):
    all_products =Products.objects.all()
    context = {
        'products': all_products,
    }
    return render(request, 'products/list_products.html', context= context)

def create_category(request, name):
   Category.objects.create(name = name)
   return HttpResponse('Categoria creada')

def list_categories(request):
    all_categories  = Category.objects.all()
    context = {
        'categories' : all_categories
    }
    return render(request, 'categories/list_categories.html', context=context)



    