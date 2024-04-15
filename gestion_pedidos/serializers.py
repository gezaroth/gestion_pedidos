from rest_framework import serializers
from gestion_articulos_pedidos.models import Articulo, Pedido, ArticuloPedido

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'