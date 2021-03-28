from django.urls import path
from apps.productos.views.productos_compras_view import ProdutosCompraView

urlpatterns = [
  path('productos_compra/',ProdutosCompraView.as_view(),name='productos_compra'),
]