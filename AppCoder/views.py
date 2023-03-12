from django.shortcuts import render

from django.shortcuts import HttpResponse

from AppCoder.models import Automotor
# Create your views here.

#hipervinculos index
def index(request):
    return render(request, "AppCoder/index.html")

def busqueda(request):
    return render(request, "AppCoder/busqueda.html")

def usuarios(request):
    return render(request, "AppCoder/usuarios.html")

def registro(request):
    return render(request, "AppCoder/registro.html")

# formularios 

def Buscar(request):
    
    if request.GET["patente"]:

        npatente = request.GET["patente"]
        automotor = Automotor.objects.filter(npatente_itcontains = npatente)

    else:
        respueta = " No se encontro la patente "
    return HttpResponse(respueta)


