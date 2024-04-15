from django.db import models

class Articulo(models.Model):
    referencia = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_sin_impuestos = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto_aplicable = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    @property
    def precio_con_impuestos(self):
        return self.precio_sin_impuestos * (1 + self.impuesto_aplicable / 100)

class Pedido(models.Model):
    articulos = models.ManyToManyField(Articulo, through='ArticuloPedido')
    cantidad_articulos = models.PositiveIntegerField(default=0)
    precio_total_sin_impuestos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_total_con_impuestos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def actualizar_cantidad_articulos(self):
        self.cantidad_articulos = sum([item.cantidad for item in self.articulopedido_set.all()])
        self.save()

    def actualizar_precio_total(self):
        self.precio_total_sin_impuestos = sum([item.articulo.precio_sin_impuestos * item.cantidad for item in self.articulopedido_set.all()])
        self.precio_total_con_impuestos = sum([item.articulo.precio_con_impuestos * item.cantidad for item in self.articulopedido_set.all()])
        self.save()

class ArticuloPedido(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        super(ArticuloPedido, self).save(*args, **kwargs)
        self.pedido.actualizar_cantidad_articulos()
        self.pedido.actualizar_precio_total()

    def delete(self, *args, **kwargs):
        super(ArticuloPedido, self).delete(*args, **kwargs)
        self.pedido.actualizar_cantidad_articulos()
        self.pedido.actualizar_precio_total()
