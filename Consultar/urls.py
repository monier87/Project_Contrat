from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.Consultar, name="Consultar"),
    path('Consultar/editar', views.editar, name="editar"),
    
    
]