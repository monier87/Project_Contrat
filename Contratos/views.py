from django.shortcuts import render, HttpResponse
from django.contrib import messages
from Contratos.models import Contratos
# Create your views here.

def FormContratos(request):

    if request.method=="POST":
        cont=Contratos(numero=request.POST["numero"],importe=request.POST["importe"],fecha=request.POST["fecha"],cliente=request.POST["cliente"],observacion=request.POST["observacion"])
        
        cont.save()

    return render(request, 'contratos/Contratos.html')



 
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