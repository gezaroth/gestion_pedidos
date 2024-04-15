# En tu archivo api.py

from rest_framework import viewsets
from .models import Articulo
from gestion_pedidos.serializers import ArticuloSerializer

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
