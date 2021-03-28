from django.urls import path
from apps.compras.views.compras_list_view import ComprasViewSet

urlpatterns = [
  path('compras_compra/',ComprasViewSet.as_view({'get': 'list'}),name='compras_'),
]