from django.contrib import admin

from products.models import Products

# admin.site.register(Products) #codigo para subir  y editar en base de datos

@admin.register(Products) #edicion de admin django
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')
    list_filter = ('stock',)
    search_fields = ('name',)

