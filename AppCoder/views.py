from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Automotor
# Create your views here.

#hipervinculos index
def index(request):
    return render(request, "AppCoder/index.html")

def usuarios(request):
    return render(request, "AppCoder/usuarios.html")

def registro(request):
    return render(request, "AppCoder/registro.html")

#busqueda y buscar /view y formularios 

def busqueda(request):
    return render(request, "AppCoder/busqueda.html")

def Buscar(request):
    
    if request.GET['patente']:
        
    
        respueta = f"estoy buscando la patente numero:{ request.GET['patente'] }"

        """npatente = request.GET["patente"]
        automotor = Automotor.objects.filter(npatente_itcontains = npatente)

        return HttpResponse(respueta)"""

    else:
        respueta = " No se encontro la patente "

    return HttpResponse(respueta)


