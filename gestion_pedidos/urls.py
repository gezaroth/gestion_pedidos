from django.contrib import admin
from django.urls import path, include
from gestion_articulos_pedidos import views
from rest_framework.routers import DefaultRouter
from gestion_articulos_pedidos.api import ArticuloViewSet

router = DefaultRouter()
router.register(r'articulos', ArticuloViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('articulos/', views.articulo_list),
    path('articulos/<int:pk>/', views.articulo_detail),
    path('pedidos/', views.pedido_list),
    path('pedidos/<int:pk>/', views.pedido_detail),
]