from django.db import models
from django.utils import timezone

# Create your models here.

class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class TipoDocumento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    tipodocumento = models.ForeignKey(TipoDocumento, on_delete= models.CASCADE)
    documento = models.BigIntegerField()
    lugarresidencia = models.ForeignKey(Ciudad, on_delete= models.CASCADE)
    fechanacimiento = models.DateField()
    email = models.EmailField(max_length=30)
    telefono = models.BigIntegerField() 
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre