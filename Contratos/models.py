from django.db import models
from django.db import models
from datetime import datetime

# Create your models here.

    
class Contratos(models.Model):
    titulo = models.CharField(max_length=200, null=True, verbose_name="Titulo")
    numero = models.CharField(max_length=30, null=False, unique=True, verbose_name="Número")
    importe = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Importe")
    fecha = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="Fecha")
    cliente = models.CharField(max_length=200, null=False, verbose_name="Cliente")
    aprobado=models.BooleanField(default=False)
    observacion = models.TextField(null=True, blank=True, verbose_name="Observación")
    
    
    
    class Meta:
        verbose_name='contrato'
        verbose_name_plural='contratos'
        
    def __str__(self):
        return self.titulo
    
    
    



    
    
    
    
    
    
    
  
    
 
    

    
