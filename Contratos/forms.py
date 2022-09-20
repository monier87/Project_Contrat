from dataclasses import field
from django import forms
from .models import Contratos
from django.shortcuts import render

class consultarForm(forms.ModelForm):
    
    class Meta:
        model= Contratos
        fields=["titulo", "numero","importe","fecha","cliente","observacion"]