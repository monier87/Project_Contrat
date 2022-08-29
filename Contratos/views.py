from django.shortcuts import render
from .forms import Contratos
from django.contrib import messages
# Create your views here.
def form_Contratos(request):
    form = Contratos(request.POST or None)
    if form.is_valid():
        form.save()		
        messages.success(request, 'Contrato insertada correctamente.')
        form = Contratos()
    else:
        messages.error(request, 'Error al insertar Contrato. Revise los datos.')
    context = {'form': form }      
    return render(request, 'Contratos.html', context)




 
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