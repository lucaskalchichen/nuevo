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
        

        patente = request.GET['patente'] 
        automotor = Automotor.objects.filter(npatente = patente)

        return render(request, "AppCoder/Busqueda.html", {"vehiculo":automotor,"patente":patente})

    else:
        respueta = " No se encontro la patente "

        return HttpResponse(respueta)


