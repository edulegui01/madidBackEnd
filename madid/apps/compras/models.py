from django.db import models
from apps.productos.models import Productos
from apps.proveedores.models import Proveedores
from apps.empleados.models import Empleados
# Create your models here.

class Compras(models.Model):
  id = models.AutoField(primary_key=True)
  fecha = models.DateField(max_length=20,default="234")
  id_proveedores = models.ForeignKey(Proveedores,on_delete=models.CASCADE,null=True)
  monto_total = models.IntegerField()
  cedula_empleado = models.ForeignKey(Empleados,on_delete=models.CASCADE, null=True)

  def __str__(self):
    return str(self.id)


class DetalleCompra(models.Model):
  id_compra = models.ForeignKey(Compras,on_delete=models.CASCADE)
  id_producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
  cantidad = models.IntegerField()
  precio_compra = models.IntegerField()

  def __str__(self):
    return 'id_compra: {} id_producto: {}'.format(self.cantidad,self.id_producto)
