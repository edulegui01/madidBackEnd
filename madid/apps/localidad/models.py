from django.db import models

class Localidad(models.Model):
  id_localidad = models.AutoField(primary_key=True)
  ciudad = models.CharField(max_length=40)
  departamento = models.CharField(max_length=40)
