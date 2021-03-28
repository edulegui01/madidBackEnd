from rest_framework import serializers
from apps.proveedores.models import Proveedores

class ProveedoresCompraSerializer(serializers.ModelSerializer):
  class Meta:
    model = Proveedores
    fields = ['id','nombre']
