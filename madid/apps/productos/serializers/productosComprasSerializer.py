from rest_framework import serializers
from apps.productos.models import Productos


class ProductosComprasSerializer(serializers.ModelSerializer):
  class Meta:
    model = Productos
    fields = ['id','nombre']
    