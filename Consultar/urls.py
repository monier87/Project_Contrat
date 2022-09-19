from django.urls import path 
 
from . import views
 
urlpatterns = [
     
    path('Consultar/Consultar/', views.Consultar, name='Consultar'),
    path('Consultar/eliminar/<int:contratos_id>/', views.eliminar, name='eliminar'),
    path('Consultar/editar/<int:contratos_id>/', views.editar, name='editar'),
 
]