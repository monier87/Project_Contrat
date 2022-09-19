from multiprocessing import context
from django.shortcuts import render, redirect
from Contratos.models import Contratos
from Contratos.views import FormContratos


def Consultar(request):
    contratos=Contratos.objects.all()
    context= {'contratos':contratos}    
    return render(request, 'Consultar/Consultar.html', context) 



def editar (request, contratos_id):
    p = Contratos.objects.get(id=contratos_id)
    if request.method == "POST":
     form = FormContratos(request.POST,instance=p)
     if form.is_valid():
         form.save() #aqui estas guardando diractamente el formulario en la base de datos
         return redirect ('Consultar')
    else:
        form = FormContratos(instance=p) 

    ctx = {'formulario' : form}

    return render("Consultar/editar.html", ctx)


def eliminar(request, contratos_id):
    contrato=Contratos.objects.get(id=contratos_id)
    contrato.delete()
    return redirect("Consultar")