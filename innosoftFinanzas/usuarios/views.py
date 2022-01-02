from django.shortcuts import redirect, render
from usuarios.models import Usuario
import logging

def login(request):
    context = {}
    if not "session" in request.session.keys():
        request.session["session"] = "NA"
    return render(request,"usuarios/login.html",context)

#TODO: Validate password
#TODO: Make sure there is no sql inject

def handleLogin(request):
    context = {}
    if request.method == "POST":
        form = request.POST
        #if form.is_valid():
        #data = form.cleaned_data
        #Check si usuario existe
        if Usuario.objects.filter(uvus=form["uvus"]).exists():
            passwordHash = hash(form["password"])
            if Usuario.objects.get(uvus=form["uvus"]).passwordHash==passwordHash:
            #if True:
                request.session["session"]=Usuario.objects.get(uvus=form["uvus"]).rol
                return render(request,"usuarios/loginSuccesful.html",context)
            else: 
                context["errorDescription"]="Contraseña errónea"
                request.session["session"] = "NA"
        else:
            context["errorDescription"]="El usuario no se encuentra en la base de datos"
    return render(request,"usuarios/loginError.html",context)

def loginError(request):
    context = {}
    return render(request,"usuarios/loginError.html",context)

def loginSuccesful(request):
    context = {}
    return render(request,"usuarios/loginSuccesful.html",context)

def register(request):
    context = {}
    return render(request,"usuarios/register.html",context)

def handleRegistration(request):
    context = {}
    if request.method == "POST":
        form = request.POST
        if Usuario.objects.filter(uvus=form["uvus"]).exists():
            user : Usuario = Usuario.objects.get(uvus=form["uvus"])
            user.passwordHash = hash(form["password"])
            user.save()
            #logging.warning(hash(form["password"]))
            #logging.warning(user.passwordHash)
            return render(request,"usuarios/login.html",context)
        else:
            context["errorDescription"] = "Usuario no se encuentra en la base de datos"
            return render(request, "usuarios/registerError.html", context)
