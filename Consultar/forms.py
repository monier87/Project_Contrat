from dataclasses import field
from django import forms
from Contratos.models import Contratos
from django.shortcuts import render

class EditarForm(forms.ModelForm):
    
    class Meta:
        model= Contratos
        fields=["titulo", "numero","importe","fecha","cliente","observacion"]