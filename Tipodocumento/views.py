from unittest import loader
from django.shortcuts import render, redirect
from .models import tipo_documento
from django.http import HttpResponse
from multiprocessing import context
from re import template 
from django.template import loader

# Create your views here.
def documento(request):
    documento = tipo_documento.objects.all()
    template = loader.get_template('TD/documento.html')
    context = {'documentos': documento,}
    return HttpResponse(template.render(context, request))

def nuevo_documento(request):
    nuevo_nombre = request.POST["nombreTD"]
    nueva_descripcion = request.POST["descripcionTD"]
    dc = tipo_documento(nombre=nuevo_nombre, descripcion=nueva_descripcion)
    dc.save()
    return redirect('/')
   
def delete_documento(request, documento_id):
    dc = tipo_documento.objects.get(id = documento_id)
    dc.delete()
    return redirect('/')