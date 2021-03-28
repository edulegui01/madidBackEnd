from apps.proveedores.serializers.proveedores_compra_serializer import ProveedoresCompraSerializer
from rest_framework import generics
from rest_framework.response import  Response


class ProveedoresCompraView(generics.ListAPIView):
  serializer_class = ProveedoresCompraSerializer

  def get_queryset(self):
    model = self.get_serializer().Meta.model
    return model.objects.all()