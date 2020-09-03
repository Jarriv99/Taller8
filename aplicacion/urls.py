from django.urls import path
from .views import *
from .forms import PersonaForm
from . import views

urlpatterns = [
    path('', home,name= "index"),
    path('crear_persona/',CreatePersona.as_view(), name= "crear_persona"),
    path('listar_persona/',ListPersona.as_view(), name= "listar_persona"),
    path('editar_persona/<int:pk>/',UpdatePersona.as_view(), name= "editar_persona"),
    path('eliminar_persona/<int:pk>/',DeletePersona.as_view(), name= "eliminar_persona"),
]