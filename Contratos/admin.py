from django.contrib import admin

from .models import Contratos, Provincia, Proveedor


# Register your models here.

#class ContratosAdmin(admin.ModelAdmin):
    #readonly_fields=('Creado', 'Modificado')
    
admin.site.register([Contratos,Provincia, Proveedor])
