from django.urls import path

from proyectoWebapp import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    
     path('admin/', admin.site.urls),
    
    path('', views.Inicio, name="Inicio"),
    path('Consultar', views.Consultar, name="Consultar"),
    path('Entidades', views.Entidades, name="Entidades"),
    path('Contratos', views.Contratos, name="Contratos"),
    path('Reportes', views.Reportes, name="Reportes"),
    path('Clasificadores', views.Clasificadores, name="Clasificadores"),
    path('Seguridad', views.Seguridad, name="Seguridad"),
    path('Ayuda', views.Ayuda, name="Ayuda"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
