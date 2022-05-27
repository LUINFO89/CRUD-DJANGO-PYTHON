from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Libros
from .forms import LibrosForm



# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')
def nosotros (request):
    return render(request,'paginas/nosotros.html')



def libros (request):
    libros = Libros.objects.all()
    print(libros)
    return render(request,'libros/index.html', {'libros':libros})
def crear (request):
    formulario = LibrosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request,'libros/crear.html',{'formulario':formulario})


def editar (request,id):
    libro = Libros.objects.get(id=id)
    formulario = LibrosForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request,'libros/editar.html',{'formulario':formulario})

def eliminar (request,id):
    libros = Libros.objects.get(id=id)
    libros.delete()
    return redirect('libros')

