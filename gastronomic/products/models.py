from django.db import models

from enterprises.models import Enterprise

# Create your models here.


class Product(models.Model):
    """Clase Producto"""
    name = models.CharField(max_length=45, help_text='nombre')
    price = models.PositiveBigIntegerField(help_text='precio')
    ingredients = models.TextField(help_text='ingredientes')
    preparation = models.TextField(null=True, blank=True, help_text='preparación')
    estimated_time = models.TimeField(help_text='tiempo estimado')

    # Relaciones
    enterprise = models.ForeignKey(
        Enterprise,
        related_name='products',
        on_delete=models.CASCADE
    )
    accompaniments = models.ManyToManyField(
        'self',
        related_name='products',
        help_text='acompañamientos'
    )

    def __str__(self) -> str:
        """Función que representa el objeto"""
        return self.name


class Image(models.Model):
    """Clase Imagen"""
    url = models.ImageField()

    # Relaciones
    product = models.ForeignKey(
        'Product',
        related_name='images',
        on_delete=models.CASCADE,
        help_text='producto'
    )

    def __str__(self) -> str:
        return self.url.name
