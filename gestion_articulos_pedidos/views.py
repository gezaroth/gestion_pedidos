from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Articulo, Pedido, ArticuloPedido
from gestion_pedidos.serializers import ArticuloSerializer, PedidoSerializer

@api_view(['GET', 'POST'])
def articulo_list(request):
    if request.method == 'GET':
        articulos = Articulo.objects.all()
        serializer = ArticuloSerializer(articulos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticuloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def articulo_detail(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'GET':
        serializer = ArticuloSerializer(articulo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticuloSerializer(articulo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        articulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def pedido_list(request):
    if request.method == 'GET':
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            # Guardar el pedido sin artículos primero
            pedido = serializer.save()

            # Obtener los IDs de los artículos del cuerpo de la solicitud
            articulos_ids = request.data.get('articulos', [])

            # Asociar los artículos con el pedido
            for articulo_id in articulos_ids:
                try:
                    articulo = Articulo.objects.get(id=articulo_id)
                    ArticuloPedido.objects.create(articulo=articulo, pedido=pedido, cantidad=1)
                except Articulo.DoesNotExist:
                    return Response({'error': f'El artículo con ID {articulo_id} no existe'}, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'GET':
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PedidoSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
