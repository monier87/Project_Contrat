from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from Contratos.models import Contratos
from Contratos.views import consultarForm


def Consultar(request):
    contratos=Contratos.objects.all()
    context= {'contratos':contratos}    
    return render(request, 'Consultar/Consultar.html', context) 



def eliminar(request, contratos_id):
    contrato=Contratos.objects.get(id=contratos_id)
    contrato.delete()
    return redirect("Consultar")



def editar(request, contratos_id):
    contrato=Contratos.objects.get(id=contratos_id)
    if request.method=="POST":
        form=consultarForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contrato editado correctamente.')
            return redirect('Contratos')
    else:
        form= consultarForm(instance=contrato)
    
    context={'form': form}
    return render(request, 'Consultar/editar.html', context)
        
        
    