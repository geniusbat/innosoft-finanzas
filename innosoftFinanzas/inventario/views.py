from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request,num=-1):
    context = {}
    return render(request,"inventario/index.html",context)