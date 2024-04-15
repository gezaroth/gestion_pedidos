from django.contrib import admin
from .models import Articulo, Pedido, ArticuloPedido

admin.site.register(Articulo)
admin.site.register(Pedido)
admin.site.register(ArticuloPedido)
