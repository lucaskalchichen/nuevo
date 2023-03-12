from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "AppCoder/index.html")

def busqueda(request):
    return render(request, "AppCoder/busqueda.html")

def usuarios(request):
    return render(request, "AppCoder/usuarios.html")

def registro(request):
    return render(request, "AppCoder/registro.html")



