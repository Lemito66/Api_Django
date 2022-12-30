from django.db import models

# Create your models here.
class Articulos(models.Model):
    codigo_articulo = models.CharField(max_length=500, verbose_name='Código del artículo')
    nombre_articulo = models.CharField(max_length=500, verbose_name='Nombre del artículo')
    descripcion_articulo = models.CharField(max_length=500, verbose_name='Descripción del artículo')
    cantidad_disponible_del_articulo = models.IntegerField(verbose_name='Cantidad disponible del artículo')
    
    def __str__(self) -> str:
        return f'{self.nombre_articulo}'