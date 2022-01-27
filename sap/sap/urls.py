
from django.contrib import admin
from django.urls import path
from personas.views import nuevaPersona ,detallePersona, editarPersona , eliminarPersona
from webapp.views import bienvenido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='inicio'),
    path('detalle_persona/<int:id>', detallePersona),
    path('nueva_persona/', nuevaPersona),
    path('editar_persona/<int:id>', editarPersona),
    path('eliminar_persona/<int:id>', eliminarPersona)
  
]
