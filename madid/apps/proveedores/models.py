from django.db import models
from apps.localidad.models import Localidad

# Create your models here.

class Proveedores(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=30)
  direccion = models.CharField(max_length=200)
  ruc = models.IntegerField()
  telefono = models.IntegerField()
  cedula = models.IntegerField()
  email = models.EmailField()
  id_localidad = models.ForeignKey(Localidad,on_delete=models.CASCADE, null=True)
  
  def __str__(self):
    return self.nombre
