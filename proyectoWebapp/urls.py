from django.urls import path

from django.contrib import admin
from proyectoWebapp import views

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('Consultar', views.Consultar, name="Consultar"),
    path('Entidades', views.Entidades, name="Entidades"),
    path('Reportes', views.Reportes, name="Reportes"),
    path('Clasificadores', views.Clasificadores, name="Clasificadores"),
    path('Seguridad', views.Seguridad, name="Seguridad"),
    path('Ayuda', views.Ayuda, name="Ayuda"),
]