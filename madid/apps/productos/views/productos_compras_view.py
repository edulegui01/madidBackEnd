from rest_framework import generics
from apps.productos.serializers.productosComprasSerializer import ProductosComprasSerializer
from rest_framework.response import Response



class ProdutosCompraView(generics.ListAPIView):
  serializer_class = ProductosComprasSerializer

  def get_queryset(self):
    model = self.get_serializer().Meta.model
    return model.objects.all()






