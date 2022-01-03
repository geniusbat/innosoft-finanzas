from django.shortcuts import render
from sugerencias.models import Sugerencia


# TODO: Meter from usuarios

def index(request):
    context = {}
    return render(request, 'sugerencias/sugerencias.html', context)


def addSug(request):
    context = {}
    return render(request, 'sugerencias/sugerenciaFormulario.html', context)


def handleSugSubmit(request):
    context = {}
    if request.method == "POST":
        form = request.POST
        if True:  # TODO: Check user exists
            aux = Sugerencia()
            aux.sugTipo = form["sugTipo"]
            aux.description = form["sugDescription"]
            aux.save()
            return render(request, "sugerencias/sugerencias.html", context)
    else:
        context["errorDescription"] = "Algo ha salido mal, estamos trabajando en ello"
        return render(request, "sugerencias/sugerenciasError.html", context)
