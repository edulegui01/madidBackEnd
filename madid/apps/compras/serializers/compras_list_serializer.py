from rest_framework import serializers


class ComprasListSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  #fecha = serializers.DateTimeField()
  id_proveedores__nombre = serializers.CharField(max_length=100)
  id_proveedores__id_localidad__ciudad = serializers.CharField(max_length=40)
  cedula_empleado__nombre = serializers.CharField(max_length=100)
  monto_total = serializers.IntegerField()


  def to_representation(self,instanse):
    return {
      'id': instanse['id'],
      'proveedor': instanse['id_proveedores__nombre'],
      'ciudad': instanse['id_proveedores__id_localidad__ciudad'],
      'encargado': instanse['cedula_empleado__nombre'],
      'total': instanse['monto_total']
    }