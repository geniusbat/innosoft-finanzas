import logging
from django.shortcuts import render

from usuarios.models import Usuario

def index(request):
    context = {}
    if checkCredentials(request):
        return render(request,"administrador/index.html",context)
    else:
        return handleInvalidEntry(request,context)

def checkCredentials(request):
    #logging.warn("Session credentials: " + request.session["session"])
    if "session" in request.session and request.session["session"]!="NA" and request.session["session"]!="MB":
        return True
    else:
        #return False
        return True

def usuarios(request):
    if checkCredentials(request):
        context = {"usuarios":Usuario.objects.all}
        return render(request,"administrador/adminUsuarios.html",context)
    else:
        context = {}
        return handleInvalidEntry(request,context)

def modificarUsuario(request, uvus):
    context = {}
    logging.warning("uvus to modify:" + uvus)
    if checkCredentials(request):
        context["uvus"] = uvus.strip()
        return render(request,"administrador/modificarUsuario.html",context)
    else:
        return handleInvalidEntry(request,context)

def handleModificarUsuario(request):
    context = {}
    if checkCredentials(request):
        if request.method == "POST":
            form = request.POST
            if Usuario.objects.all().filter(uvus=form["uvus"].strip()).exists():
                usuario = Usuario.objects.get(uvus=form["uvus"].strip())
                usuario.uvus = form["newUvus"].strip()
                usuario.rol = form["rol"]
                usuario.save()
        return usuarios(request)
    return handleInvalidEntry(request,context)

def eliminarUsuario(request, uvus):
    context = {}
    logging.warning("uvus to modify:" + uvus)
    if checkCredentials(request):
        if Usuario.objects.filter(uvus=uvus).exists():
            user = Usuario.objects.get(uvus=uvus)
            user.delete()
        return usuarios(request)
    else:
        return handleInvalidEntry(request,context)

def nuevoUsuario(request):
    context = {}
    if checkCredentials(request):
        return render(request,"administrador/nuevoUsuario.html",context)
    else:
        return handleInvalidEntry(request,context)

def handleNuevoUsuario(request):
    context = {}
    if checkCredentials(request):
        if request.method == "POST":
            form = request.POST
            user = Usuario(uvus=form["uvus"].strip(), rol=form["rol"], passwordHash=-1)
            user.save()
        return usuarios(request)
    else:
        return handleInvalidEntry(request,context)

def handleInvalidEntry(request,context):
    return render(request,"index.html",context)