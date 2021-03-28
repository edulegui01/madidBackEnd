from rest_framework import viewsets
from apps.compras.models import Compras, DetalleCompra
from apps.proveedores.models import Proveedores
from apps.empleados.models import Empleados
from apps.compras.serializers.compras_list_serializer import ComprasListSerializer
from rest_framework.response import Response


class ComprasViewSet(viewsets.ViewSet):
  def list(self,request):
    queryset = Compras.objects.values('id','id_proveedores__nombre','id_proveedores__id_localidad__ciudad','cedula_empleado__nombre','monto_total')
    serializer = ComprasListSerializer(queryset,many=True)
    return Response(serializer.data)


 