from django.urls import include, path
from .views import *
from .forms import PersonaForm

urlpatterns = [
    path('', home,name= "index"),
    path('crear_persona/',CreatePersona.as_view(), name= "crear_persona"),
    path('listar_persona/',ListPersona.as_view(), name= "listar_persona"),
    path('editar_persona/',UpdatePersona.as_view(), name= "editar_persona"),
    path('eliminar_persona/',DeletePersona.as_view(), name= "eliminar_persona"),
]