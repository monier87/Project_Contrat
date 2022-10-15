from django.shortcuts import render, redirect
from django.views.generic import View

#Para crear el formulario de autenticacion

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

class VRegistro(View):
    
    def get(self, request):
        form=UserCreationForm()
        return render(request, "autenticacion/autenticacion.html", {"form":form})
    
    
    def post(self, request):
        form=UserCreationForm(request.POST)
         
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('Inicio')
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request, "autenticacion/autenticacion.html", {"form":form})
             
            
    
             
                
         
         
         
         
         
