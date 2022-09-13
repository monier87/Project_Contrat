from django.shortcuts import render, HttpResponse 

#from Contratos.models import Contratos 

# Create your views here.

def Inicio(request):
        
    return render(request, "proyectoWebapp/Inicio.html")

def Consultar(request):
        
    return render(request, "proyectoWebapp/Consultar.html")

def Entidades(request):
        
    return render(request, "proyectoWebapp/Entidades.html")
    

def Reportes(request):
        
    return render(request, "proyectoWebapp/Reportes.html")

def Clasificadores(request):
        
    return render(request, "proyectoWebapp/Clasificadores.html")

def Seguridad(request):
      
    return render(request, "proyectoWebapp/Seguridad.html")

def Ayuda(request):
    
    return render(request, "proyectoWebapp/Ayuda.html")
