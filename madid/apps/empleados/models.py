from django.db import models
from apps.localidad.models import Localidad

class Empleados(models.Model):
  cedula = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  direccion = models.CharField(max_length=40)
  fecha_ingre = models.DateTimeField()
  fecha_nacimi = models.DateTimeField()
  rol = models.CharField(max_length=20)
  telefono = models.IntegerField()
  barrio = models.CharField(max_length=40)
  id_localidad = models.ForeignKey(Localidad,on_delete=models.CASCADE)

