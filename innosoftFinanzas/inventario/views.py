import json

from django.http import HttpResponse
from django.shortcuts import render

from inventario.models import Producto,Categoria
# Create your views here.

def formProducto(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = request.POST

        if Categoria.objects.filter(categoria=form['categoria']).exists():
            categoria = Categoria.objects.get(categoria=form['categoria'])
            producto = Producto(nombre=form["nombre"].strip(), categoria=categoria, unidades=form["unidades"], valorMonetario=form["valorMonetario"], descripcion=form["descripcion"])
            producto.save()

        return listProducto(request)
    else:
        form = Producto() # Unbound form

        return render(request, 'inventario/nuevoProducto.html', {'form': form,"categorias": Categoria.objects.all})

def formCategoria(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = request.POST

        categoria = Categoria(categoria=form['categoria'])

        categoria.save()

        return listProducto(request)
    else:
        form = Categoria() # Unbound form

        return render(request, 'inventario/nuevoProducto.html', {'form': form})

def modificarProducto(request, id):
    if Producto.objects.filter(id=id).exists():
        producto = Producto.objects.get(id=id)
        context = {'id':id,'nombre': producto.nombre,'categoria':producto.categoria.categoria , 'unidades': producto.unidades,'valorMonetario': producto.valorMonetario,'descripcion': producto.descripcion}
        data = json.dumps(context)
        return HttpResponse(data, status=200)
       # return render(request, 'inventario/modificarProducto.html', {'id':id,'producto': producto,"categorias": Categoria.objects.all})

def handlemodificarProducto(request):

    if request.method == 'POST':  # si el usuario está enviando el formulario con datos
        form = request.POST

        if Producto.objects.filter(id=form['id']).exists():
            if Categoria.objects.filter(categoria=form['categoria']).exists():
                categoria = Categoria.objects.get(categoria=form['categoria'])
                producto = Producto.objects.get(id=form['id'])
                producto.nombre = form["nombre"].strip()
                producto.categoria = categoria
                producto.unidades = form["unidades"]
                producto.valorMonetario = form["valorMonetario"]
                producto.descripcion = form["descripcion"]
                producto.save()

            return listProducto(request)

def listProducto(request):
    context = {"productos": Producto.objects.all,"categorias": Categoria.objects.all}
    return render(request, "inventario/listadoProductos.html", context)

def eliminarProducto(request, id):
    context = {}

    if Producto.objects.filter(id=id).exists():
        producto = Producto.objects.get(id=id)
        producto.delete()
        return listProducto(request)
    else:
        return listProducto(request)

def eliminarCategoria(request, id):
    context = {}

    if Categoria.objects.filter(id=id).exists():
        categoria = Categoria.objects.get(id=id)
        categoria.delete()
        return listProducto(request)
    else:
        return listProducto(request)
