from django.db import models


class Categoria(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name




class Productos(models.Model):
    nombre = models.CharField( max_length=50)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    precio_compra = models.DecimalField( max_digits=7, decimal_places=2)
    precio_venta = models.DecimalField( max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name 
    