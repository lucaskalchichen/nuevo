from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Automotor,Usuario

from AppCoder.forms import FormAutomotor,FormUsuario

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
    

# registro de vehiculo

def Vehiculo(request):

    if request.method == 'POST':
        
        form = FormAutomotor(request.POST)

        print(form)

        if form.is_valid:

            info = form.cleaned_data

            vehiculo = Automotor(user=info['user'] ,nchasis=info['nchasis'], nmotor=info['nmotor'] , npatente=info['npatente'] , ano=info['ano'])

            vehiculo.save()

            return render(request, "AppCoder/index.html")
    
    else:

        context ={
            "form": FormAutomotor(),
        }
    
        return render(request, "AppCoder/registro.html", context)


#registro de usuario

def User(request):

    if request.method == 'POST':
        
        form = FormUsuario(request.POST)

        print(form)

        if form.is_valid:

            info = form.cleaned_data

            usuario = Usuario(user=info['user'] ,nombre=info['nombre'], apellido=info['apellido'] , dni=info['dni'])

            usuario.save()

            return render(request, "AppCoder/index.html")
    
    else:

        context ={
            "form": FormUsuario(),
        }
    
        return render(request, "AppCoder/registro.html", context)

