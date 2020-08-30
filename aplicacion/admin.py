from django.contrib import admin
from .models import Persona, Ciudad, TipoDocumento

# Register your models here.

@admin.register(Persona)
class ProductoAdmin(admin.ModelAdmin):
    """Persona admin."""

    list_display = ('id', 'nombre', 'apellido', 'tipodocumento', 'documento', 'lugarresidencia', 'fechanacimiento', 'email', 'telefono', 'usuario', 'password')

@admin.register(Ciudad)
class SandwichesAdmin(admin.ModelAdmin):
    """Ciudad admin."""

    list_display = ('id', 'nombre', 'descripcion')

@admin.register(TipoDocumento)
class PreciosAdmin(admin.ModelAdmin):
    """TipoDocumento admin."""

    list_display = ('id', 'nombre', 'descripcion')