from django.shortcuts import render, redirect
from Contratos.models import Contratos
from django.shortcuts import redirect

# Create your views here.

def Consultar(request):
    
    consultar=Contratos.objects.all()
    return render(request, "Consultar/Consultar.html", {"consultar": consultar})


    
    
def editar(request):
    return render(request, "Consultar/editar.html")



def agregar_contrato(request, contratos_id):
    
    contrato=Contratos(request)

    contrato=Contratos.objects.get(id=contratos_id)

    Contratos.agregar(contratos=contrato)

    return redirect("Consultar")