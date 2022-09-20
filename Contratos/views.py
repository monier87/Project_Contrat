from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import consultarForm
from .models import Contratos
# Create your views here.

def FormContratos(request):

    if request.method=="POST":
        form= consultarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contrato insertado correctamente.')
            return redirect('Contratos')
    else:
        form= consultarForm()
    
    context={'form': form}
    return render(request, 'contratos/Contratos.html', context)



 
#def form_Contratos(request):
    #form = Contratos(request.POST or None)
    #if form.is_valid():
        #form.save()		
        #messages.success(request, 'Contrato insertada correctamente.')
        #form = Contratos()
    #else:
        #messages.error(request, 'Error al insertar Contrato. Revise los datos.')
    #context = {'form': form }      
    #return render(request, 'Contratos.html', context)