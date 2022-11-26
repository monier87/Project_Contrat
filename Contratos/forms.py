from dataclasses import field
from django import forms
from .models import Contratos, Provincia, Proveedor
from django.shortcuts import render

class consultarForm(forms.ModelForm):
    
    class Meta:
        model= Contratos
        fields=["titulo","numero","importe","proveedores","fecha","observacion"]