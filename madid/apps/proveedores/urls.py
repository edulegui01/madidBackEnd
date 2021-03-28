from django.urls import path
from apps.proveedores.views.proveedores_compra_view import ProveedoresCompraView

urlpatterns = [
  path('proveedores_compra/',ProveedoresCompraView.as_view())
]